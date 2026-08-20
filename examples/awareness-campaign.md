# Awareness Campaign Example

This campaign is optimized for high-level brand exposure and content distribution.

## Campaign Object (JSON Representation)
```json
{
  "identity": {
    "campaign_id": "cmp-awareness-002",
    "name": "State of Sales Account Intelligence Report 2026",
    "status": "LIVE",
    "version": "1.0.0",
    "created_at": "2026-08-20T08:00:00Z",
    "updated_at": "2026-08-20T09:00:00Z",
    "approved_at": "2026-08-20T08:30:00Z",
    "completed_at": null
  },
  "references": {
    "strategy_reference": "strat-2026-q3-awareness",
    "positioning_reference": "pos-acct-intel-v1",
    "icp_reference": "icp-sales-leaders",
    "messaging_reference": "msg-state-of-sales"
  },
  "strategy": {
    "objective": "Awareness",
    "strategic_goal": "Establish authority in Sales Intelligence market."
  },
  "audience": {
    "ICP": "B2B SaaS companies, 20-100 employees, using Salesforce",
    "persona": "Sales Operations / VP Sales / SDR Managers",
    "segment": "Broad sales organization leaders",
    "inclusion_criteria": [
      "Target list of B2B SaaS companies",
      "Salesforce users"
    ],
    "exclusion_criteria": [
      "Existing customers",
      "Competitors",
      "Students",
      "Agencies"
    ]
  },
  "channel": {
    "primary": "LinkedIn Sponsored Content",
    "secondary": "Newsletter Ad",
    "distribution_method": "Paid Social + Newsletter placement",
    "why": "Target personas consume educational content on LinkedIn and specialized sales newsletters.",
    "expected_role": "Primary channel driving downloads, secondary driving secondary impressions."
  },
  "messaging": {
    "core_message": "Read the 2026 Sales Intelligence Benchmarks.",
    "pain": "Sales teams rely on outdated lists, wasting 40% of outbound effort.",
    "outcome": "Benchmarks and data-backed insights to guide outbound efficiency.",
    "differentiator": "Direct telemetry data from 500+ B2B orgs.",
    "proof": "Backed by data from over 1.2M outbound outreach messages analyzed."
  },
  "assets": {
    "required": [
      {
        "asset_id": "ast-pdf-01",
        "purpose": "State of Sales PDF Report",
        "audience": "VP Sales / Sales Ops",
        "message": "Outbound benchmarks 2026.",
        "CTA": "Read the report",
        "format": "PDF / Gated ebook",
        "owner": "Execution Agent",
        "status": "APPROVED",
        "dependency": null
      }
    ],
    "optional": []
  },
  "CTA": {
    "primary": "Read the report",
    "destination": "https://gtmos-analytics.com/state-of-sales-2026",
    "conversion_event": "Report Downloaded"
  },
  "measurement": {
    "north_star_metric": {
      "name": "Market Share Share-of-Voice",
      "metric_type": "North Star",
      "class": "Outcome",
      "target": 0.15,
      "baseline": 0.08,
      "actual": 0.09,
      "attribution": "Brand Mention Tracker"
    },
    "primary_metric": {
      "name": "Total Report Downloads",
      "metric_type": "Primary Success",
      "class": "Outcome",
      "target": 1000,
      "baseline": 0,
      "actual": 120,
      "attribution": "HubSpot Form"
    },
    "secondary_metrics": [
      {
        "name": "Form Submission Rate",
        "metric_type": "Secondary",
        "class": "Outcome",
        "target": 0.22,
        "baseline": 0.15,
        "actual": 0.18,
        "attribution": "Google Analytics"
      }
    ],
    "diagnostic_metrics": [
      {
        "name": "Ad Impressions",
        "metric_type": "Diagnostic",
        "class": "Output",
        "target": 100000,
        "baseline": 0,
        "actual": 15000,
        "attribution": "LinkedIn Ad Manager"
      }
    ],
    "guardrail_metrics": [
      {
        "name": "Cost Per Download",
        "metric_type": "Guardrail",
        "class": "Outcome",
        "target": 8.0,
        "baseline": 12.0,
        "actual": 9.5,
        "attribution": "Spend / Downloads"
      }
    ]
  },
  "execution": {
    "tasks": [
      {
        "task_id": "T01",
        "description": "Upload report PDF",
        "owner": "Execution Agent",
        "asset": "ast-pdf-01",
        "dependency": [],
        "status": "DONE",
        "priority": "HIGH",
        "due_date": "2026-08-10",
        "verification": "PDF is publicly downloadable from AWS S3."
      },
      {
        "task_id": "T02",
        "description": "Launch LinkedIn Campaign",
        "owner": "Execution Agent",
        "asset": null,
        "dependency": ["T01"],
        "status": "DONE",
        "priority": "HIGH",
        "due_date": "2026-08-11",
        "verification": "LinkedIn campaign is active and delivering."
      }
    ],
    "owners": ["Execution Agent"],
    "dependencies": [],
    "launch_date": "2026-08-11",
    "launch_status": "LAUNCH READY"
  }
}
```
