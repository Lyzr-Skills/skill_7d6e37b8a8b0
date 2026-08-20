# Activation Campaign Example

This campaign is optimized for product onboarding and activation milestones.

## Campaign Object (JSON Representation)
```json
{
  "identity": {
    "campaign_id": "cmp-activation-003",
    "name": "Integration Setup Onboarding Campaign",
    "status": "LIVE",
    "version": "1.0.0",
    "created_at": "2026-08-20T08:00:00Z",
    "updated_at": "2026-08-20T09:00:00Z",
    "approved_at": "2026-08-20T08:30:00Z",
    "completed_at": null
  },
  "references": {
    "strategy_reference": "strat-2026-q3-activation",
    "positioning_reference": "pos-integration-setup",
    "icp_reference": "icp-salesforce-admins",
    "messaging_reference": "msg-one-click-integration"
  },
  "strategy": {
    "objective": "Activation",
    "strategic_goal": "Increase 14-day Salesforce integration activation rate to 60%"
  },
  "audience": {
    "ICP": "Salesforce Admins / Revenue Operations managers who registered in last 3 days",
    "persona": "Salesforce Admin",
    "segment": "New signups without active Salesforce integration",
    "inclusion_criteria": [
      "User status = Signed Up",
      "Salesforce integration connected = False",
      "Signup date within past 72 hours"
    ],
    "exclusion_criteria": [
      "Users who already connected Salesforce",
      "Sandbox / test accounts"
    ]
  },
  "channel": {
    "primary": "In-app Notification",
    "secondary": "Transactional Email",
    "distribution_method": "Automated lifecycle trigger",
    "why": "Users are already inside the application or actively checking their inbox post-signup.",
    "expected_role": "In-app prompt drives immediate setup, email acts as backup reminder."
  },
  "messaging": {
    "core_message": "Connect Salesforce to unlock account buying signals.",
    "pain": "Accounts without Salesforce integration don't sync signal updates automatically.",
    "outcome": "One-click connection retrieves pipeline health metrics automatically.",
    "differentiator": "Zero API coding required.",
    "proof": "95% of active users activate this within the first hour."
  },
  "assets": {
    "required": [
      {
        "asset_id": "ast-email-01",
        "purpose": "Onboarding Email 1",
        "audience": "New signups",
        "message": "Start Salesforce integration setup.",
        "CTA": "Start setup",
        "format": "HTML transactional email",
        "owner": "Execution Agent",
        "status": "APPROVED",
        "dependency": null
      }
    ],
    "optional": []
  },
  "CTA": {
    "primary": "Start setup",
    "destination": "https://gtmos-analytics.com/app/integrations/salesforce",
    "conversion_event": "Salesforce Connected"
  },
  "measurement": {
    "north_star_metric": {
      "name": "LTV / Retention rate",
      "metric_type": "North Star",
      "class": "Outcome",
      "target": 0.85,
      "baseline": 0.80,
      "actual": null,
      "attribution": "14-day signup retention cohort"
    },
    "primary_metric": {
      "name": "Integration Activation Rate",
      "metric_type": "Primary Success",
      "class": "Outcome",
      "target": 0.60,
      "baseline": 0.42,
      "actual": 0.45,
      "attribution": "App Segment Event"
    },
    "secondary_metrics": [
      {
        "name": "In-app Modal Click-Through Rate",
        "metric_type": "Secondary",
        "class": "Outcome",
        "target": 0.35,
        "baseline": 0.20,
        "actual": 0.28,
        "attribution": "Segment Event"
      }
    ],
    "diagnostic_metrics": [
      {
        "name": "Email Open Rate",
        "metric_type": "Diagnostic",
        "class": "Output",
        "target": 0.45,
        "baseline": 0.38,
        "actual": 0.40,
        "attribution": "Customer.io"
      }
    ],
    "guardrail_metrics": [
      {
        "name": "Email Unsubscribe Rate",
        "metric_type": "Guardrail",
        "class": "Outcome",
        "target": 0.01,
        "baseline": 0.005,
        "actual": 0.006,
        "attribution": "Customer.io"
      }
    ]
  },
  "execution": {
    "tasks": [
      {
        "task_id": "T01",
        "description": "Configure CRM webhook trigger",
        "owner": "Execution Agent",
        "asset": null,
        "dependency": [],
        "status": "DONE",
        "priority": "HIGH",
        "due_date": "2026-08-12",
        "verification": "Webhook fires when user signs up."
      },
      {
        "task_id": "T02",
        "description": "Set up onboarding flow emails",
        "owner": "Execution Agent",
        "asset": "ast-email-01",
        "dependency": ["T01"],
        "status": "DONE",
        "priority": "HIGH",
        "due_date": "2026-08-14",
        "verification": "Email sequence tests successfully."
      }
    ],
    "owners": ["Execution Agent"],
    "dependencies": [],
    "launch_date": "2026-08-15",
    "launch_status": "LAUNCH READY"
  }
}
```
