# Channel Selection Framework

Determines primary and secondary channels based on reasoning over ICP, buyer behavior, campaign objective, and available resources.

## Selection Matrix

- **LinkedIn Outbound**
  - **ICP**: B2B Executives, Managers.
  - **Buyer Behavior**: High professional network usage.
  - **Objective**: Pipeline generation.
  
- **Cold Email**
  - **ICP**: Mid-level operational leaders, tech roles.
  - **Buyer Behavior**: High email responsiveness.
  - **Objective**: Pipeline/lead generation.
  
- **Search Ads**
  - **ICP**: Active solution seekers.
  - **Buyer Behavior**: Intent-driven queries.
  - **Objective**: High intent lead/pipeline generation.

## Recommendation Reasoning Flow
`ICP + Buyer Behavior + Objective + Message + Available Resources -> Recommendation`

If the strategy already explicitly designates the channel (e.g. "Launch LinkedIn campaign"), the execution skill MUST execute that channel and skip recommendation logic.
