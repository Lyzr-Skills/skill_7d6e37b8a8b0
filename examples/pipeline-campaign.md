# Pipeline Generation Campaign Example

This campaign is fully mapped from an approved strategy and positioning.

## Campaign Object (JSON Representation)
```json
{
  "identity": {
    "campaign_id": "cmp-pipeline-001",
    "name": "VP Sales Account Intelligence Launch",
    "status": "LIVE",
    "version": "1.0.0",
    "created_at": "2026-08-20T10:00:00Z",
    "updated_at": "2026-08-20T12:00:00Z",
    "approved_at": "2026-08-20T11:00:00Z",
    "completed_at": null
  },
  "references": {
    "strategy_reference": "strat-2026-q3-pipeline",
    "positioning_reference": "pos-acct-intel-v1",
    "icp_reference": "icp-sales-leaders",
    "messaging_reference": "msg-val-prop-outbound"
  },
  "strategy": {
    "objective": "Pipeline Generation",
    "strategic_goal": "Generate $500k in qualified sales pipeline"
  },
  "audience": {
    "ICP": "B2B SaaS companies, 20-100 employees, using Salesforce",
    "persona": "VP Sales / Head of Revenue",
    "segment": "Scaling outbound sales teams hiring SDRs",
    "inclusion_criteria": [
      "Target list of B2B SaaS companies",
      "Salesforce listed as technology in stack",
      "Job listings open for SDRs"
    ],
    "exclusion_criteria": [
      "Existing customers",
      "Competitors",
      "Students",
      "Agencies"
    ]
  },
  "channel": {
    "primary": "LinkedIn Outbound",
    "secondary": "Cold Email",
    "distribution_method": "1-to-many targeted outreach",
    "why": "VP Sales are highly active on LinkedIn and email, and the messaging requires professional context.",
    "expected_role": "Primary channel drive demo bookings, secondary supports follow-ups."
  },
  "messaging": {
    "core_message": "Give every rep the context needed to move deals.",
    "pain": "SDRs spend hours researching accounts manually, resulting in low relevance outbound.",
    "outcome": "Automated account intelligence delivered directly inside Salesforce CRM.",
    "differentiator": "Real-time buying signals directly linked to Salesforce accounts.",
    "proof": "Used by 50+ scaling SaaS companies to increase outbound reply rates by 35%."
  },
  "assets": {
    "required": [
      {
        "asset_id": "ast-lp-01",
        "purpose": "Campaign Landing Page",
        "audience": "VP Sales landing from outreach",
        "message": "Give every rep context to move deals.",
        "CTA": "Book a Demo",
        "format": "Web Page",
        "owner": "Execution Agent",
        "status": "APPROVED",
        "dependency": "t-copy-approval"
      },
      {
        "asset_id": "ast-li-01",
        "purpose": "LinkedIn Outreach Sequence",
        "audience": "VP Sales / Head of Revenue",
        "message": "Buying signals inside Salesforce.",
        "CTA": "Book a Demo",
        "format": "Direct Message Script",
        "owner": "Execution Agent",
        "status": "APPROVED",
        "dependency": null
      }
    ],
    "optional": []
  },
  "CTA": {
    "primary": "Book a demo",
    "destination": "https://gtmos-analytics.com/demo-booking",
    "conversion_event": "Qualified Demo Booked"
  },
  "measurement": {
    "north_star_metric": {
      "name": "Qualified Pipeline Value",
      "metric_type": "North Star",
      "class": "Outcome",
      "target": 500000,
      "baseline": 0,
      "actual": 120000,
      "attribution": "Opportunity Source = Campaign-001"
    },
    "primary_metric": {
      "name": "Qualified Demos Booked",
      "metric_type": "Primary Success",
      "class": "Outcome",
      "target": 50,
      "baseline": 0,
      "actual": 12,
      "attribution": "Calendly Event"
    },
    "secondary_metrics": [
      {
        "name": "Meeting Attended Rate",
        "metric_type": "Secondary",
        "class": "Outcome",
        "target": 0.85,
        "baseline": 0.80,
        "actual": 0.83,
        "attribution": "CRM Status"
      }
    ],
    "diagnostic_metrics": [
      {
        "name": "Click-Through Rate (CTR)",
        "metric_type": "Diagnostic",
        "class": "Output",
        "target": 0.05,
        "baseline": 0.03,
        "actual": 0.048,
        "attribution": "Campaign Tracker"
      }
    ],
    "guardrail_metrics": [
      {
        "name": "Cost Per Demo",
        "metric_type": "Guardrail",
        "class": "Outcome",
        "target": 250,
        "baseline": 300,
        "actual": 220,
        "attribution": "Spend / Demos"
      }
    ]
  },
  "execution": {
    "tasks": [
      {
        "task_id": "T01",
        "description": "Create campaign landing page",
        "owner": "Execution Agent",
        "asset": "ast-lp-01",
        "dependency": [],
        "status": "DONE",
        "priority": "HIGH",
        "due_date": "2026-08-15",
        "verification": "Landing page resolves and submits test lead."
      },
      {
        "task_id": "T02",
        "description": "Configure conversion tracking",
        "owner": "Execution Agent",
        "asset": null,
        "dependency": ["T01"],
        "status": "DONE",
        "priority": "CRITICAL",
        "due_date": "2026-08-16",
        "verification": "Test conversion event triggers successfully."
      },
      {
        "task_id": "T03",
        "description": "Launch campaign",
        "owner": "Execution Agent",
        "asset": null,
        "dependency": ["T01", "T02"],
        "status": "DONE",
        "priority": "HIGH",
        "due_date": "2026-08-17",
        "verification": "Outbound messages active."
      }
    ],
    "owners": ["Execution Agent"],
    "dependencies": [],
    "launch_date": "2026-08-17",
    "launch_status": "LAUNCH READY"
  }
}
```
