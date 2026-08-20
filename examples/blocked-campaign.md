# Blocked Campaign Example

This campaign is blocked because it fails the measurement readiness checks (specifically, the conversion event tracking is unverified/unconfigured).

## Campaign Object (JSON Representation)
```json
{
  "identity": {
    "campaign_id": "cmp-blocked-004",
    "name": "Outbound Acceleration Pilot",
    "status": "BLOCKED",
    "version": "1.0.0",
    "created_at": "2026-08-20T14:00:00Z",
    "updated_at": "2026-08-20T14:30:00Z",
    "approved_at": null,
    "completed_at": null
  },
  "references": {
    "strategy_reference": "strat-outbound-pilot-2026",
    "positioning_reference": "pos-outbound-v2",
    "icp_reference": "icp-sales-leaders",
    "messaging_reference": "msg-speed-outbound"
  },
  "strategy": {
    "objective": "Pipeline Generation",
    "strategic_goal": "Pilot outbound velocity optimizations for 10 target accounts"
  },
  "audience": {
    "ICP": "B2B SaaS companies, 20-100 employees, using Salesforce",
    "persona": "SDR Manager",
    "segment": "Early adopters of outbound tools",
    "inclusion_criteria": [
      "Companies with active job postings for SDRs"
    ],
    "exclusion_criteria": [
      "Existing customers"
    ]
  },
  "channel": {
    "primary": "Email Outbound",
    "secondary": "LinkedIn",
    "distribution_method": "Outreach sequence",
    "why": "Direct communication to SDR managers.",
    "expected_role": "Email triggers setup, LinkedIn provides social proof."
  },
  "messaging": {
    "core_message": "Automate SDR list verification.",
    "pain": "Manual contact list hygiene takes 5 hours per week.",
    "outcome": "Verification occurs instantly prior to sequence send.",
    "differentiator": "Real-time verify.",
    "proof": "Saves 4.5 hours per SDR per week."
  },
  "assets": {
    "required": [
      {
        "asset_id": "ast-em-out-01",
        "purpose": "Cold Email Outreach Sequence",
        "audience": "SDR Managers",
        "message": "Verify lists automatically.",
        "CTA": "Book pilot demo",
        "format": "Text email sequence",
        "owner": "Execution Agent",
        "status": "REQUIRED",
        "dependency": null
      }
    ],
    "optional": []
  },
  "CTA": {
    "primary": "Book pilot demo",
    "destination": "https://gtmos-analytics.com/pilot-demo",
    "conversion_event": "Pilot Meeting Booked"
  },
  "measurement": {
    "north_star_metric": {
      "name": "Qualified Pipeline Value",
      "metric_type": "North Star",
      "class": "Outcome",
      "target": 50000,
      "baseline": 0,
      "actual": null,
      "attribution": null
    },
    "primary_metric": {
      "name": "Pilot Meetings Booked",
      "metric_type": "Primary Success",
      "class": "Outcome",
      "target": 5,
      "baseline": 0,
      "actual": null,
      "attribution": null
    },
    "secondary_metrics": [],
    "diagnostic_metrics": [],
    "guardrail_metrics": []
  },
  "execution": {
    "tasks": [
      {
        "task_id": "T01",
        "description": "Configure conversion tracking script on /pilot-demo page",
        "owner": "Execution Agent",
        "asset": null,
        "dependency": [],
        "status": "BLOCKED",
        "priority": "CRITICAL",
        "due_date": "2026-08-21",
        "verification": "Script verified on page."
      },
      {
        "task_id": "T02",
        "description": "Launch Outreach sequence",
        "owner": "Execution Agent",
        "asset": "ast-em-out-01",
        "dependency": ["T01"],
        "status": "BLOCKED",
        "priority": "HIGH",
        "due_date": "2026-08-22",
        "verification": "Sequence active."
      }
    ],
    "owners": ["Execution Agent"],
    "dependencies": ["T01"],
    "launch_date": "2026-08-22",
    "launch_status": "BLOCKED — missing conversion tracking"
  }
}
```
