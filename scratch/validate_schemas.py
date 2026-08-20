import os
import json
import sys

# Try to import jsonschema; if not found, try to install it.
try:
    import jsonschema
    from jsonschema import RefResolver, Draft7Validator
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "jsonschema"])
    import jsonschema
    from jsonschema import RefResolver, Draft7Validator

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_tests():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schemas_dir = os.path.join(base_dir, "schemas")
    examples_dir = os.path.join(base_dir, "examples")
    
    # Load all schemas
    campaign_schema = load_json(os.path.join(schemas_dir, "campaign.schema.json"))
    task_schema = load_json(os.path.join(schemas_dir, "campaign-task.schema.json"))
    asset_schema = load_json(os.path.join(schemas_dir, "campaign-asset.schema.json"))
    measurement_schema = load_json(os.path.join(schemas_dir, "measurement.schema.json"))
    experiment_schema = load_json(os.path.join(schemas_dir, "experiment.schema.json"))

    # Setup resolver for local schema references
    schema_store = {
        "campaign.schema.json": campaign_schema,
        "campaign-task.schema.json": task_schema,
        "campaign-asset.schema.json": asset_schema,
        "measurement.schema.json": measurement_schema,
        "experiment.schema.json": experiment_schema
    }
    
    # We resolve schemas relative to the schema store
    resolver = RefResolver(base_uri="file://" + os.path.abspath(schemas_dir).replace("\\", "/") + "/", referrer=campaign_schema, store=schema_store)
    validator = Draft7Validator(campaign_schema, resolver=resolver)

    print("--- Testing JSON Schema Validations ---")

    # Load example files (which contain JSON blocks)
    def extract_json_from_md(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        start = content.find("```json")
        if start == -1:
            return None
        start += 7
        end = content.find("```", start)
        return json.loads(content[start:end].strip())

    # Scenario A: Valid Campaign (Pipeline example)
    pipeline_json = extract_json_from_md(os.path.join(examples_dir, "pipeline-campaign.md"))
    try:
        validator.validate(pipeline_json)
        print("Scenario A: Valid Campaign (pipeline-campaign.md) -> PASS (as expected)")
    except Exception as e:
        print(f"Scenario A: Valid Campaign -> FAIL: {e}")
        return False

    # Scenario B: Missing Positioning/References
    invalid_ref_json = json.loads(json.dumps(pipeline_json))
    del invalid_ref_json["references"]["positioning_reference"]
    try:
        validator.validate(invalid_ref_json)
        print("Scenario B: Missing Positioning -> Unexpected PASS")
        return False
    except jsonschema.ValidationError:
        print("Scenario B: Missing Positioning -> FAIL (Correctly validation failed)")

    # Scenario C: Missing Objective
    missing_obj_json = json.loads(json.dumps(pipeline_json))
    del missing_obj_json["strategy"]["objective"]
    try:
        validator.validate(missing_obj_json)
        print("Scenario C: Missing Objective -> Unexpected PASS")
        return False
    except jsonschema.ValidationError:
        print("Scenario C: Missing Objective -> FAIL (Correctly validation failed)")

    # Scenario D: Invalid Status
    invalid_status_json = json.loads(json.dumps(pipeline_json))
    invalid_status_json["identity"]["status"] = "INVALID_STATUS"
    try:
        validator.validate(invalid_status_json)
        print("Scenario D: Invalid Status -> Unexpected PASS")
        return False
    except jsonschema.ValidationError:
        print("Scenario D: Invalid Status -> FAIL (Correctly validation failed)")

    # Scenario E: Invalid Metric Structure
    invalid_metric_json = json.loads(json.dumps(pipeline_json))
    invalid_metric_json["measurement"]["primary_metric"]["metric_type"] = "InvalidMetricType"
    try:
        validator.validate(invalid_metric_json)
        print("Scenario E: Invalid Metric Structure -> Unexpected PASS")
        return False
    except jsonschema.ValidationError:
        print("Scenario E: Invalid Metric Structure -> FAIL (Correctly validation failed)")

    # Check Blocked Campaign Example
    blocked_json = extract_json_from_md(os.path.join(examples_dir, "blocked-campaign.md"))
    try:
        validator.validate(blocked_json)
        print("Scenario F: Blocked Campaign Example -> PASS (Valid Campaign structure, status BLOCKED)")
    except Exception as e:
        print(f"Scenario F: Blocked Campaign Example -> FAIL: {e}")
        return False

    print("\nAll schema validations passed successfully!")
    return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
