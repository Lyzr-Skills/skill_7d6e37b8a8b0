# Campaign Execution Skill

The campaign-execution skill transforms approved strategic GTM decisions into operational, executable, and measurable campaigns.

## Core Mandate
The Execution Agent does not invent GTM strategy. It consumes approved strategy and positioning, turning them into explicit execution packages.

## Operating Rules
1. **No Unapproved Execution**: Never launch or execute a campaign without an approved objective and strategy.
2. **Strategy Preservation**: Never silently change the approved ICP, positioning, or strategic objective.
3. **Inherit Messaging**: Adapt and contextualize core messaging from approved Positioning & Messaging inputs; do not create it from scratch.
4. **Measurable Conversions**: Every campaign must map to a measurable conversion event.
5. **Metric Hierarchy**: Every campaign must configure explicit metrics across North Star, Primary, Secondary, Diagnostic, and Guardrail scopes.
6. **Asset Ownership**: Every required asset must designate an owner, status, and dependency.
7. **Dependency Integrity**: Blocked tasks or incomplete prerequisites must block launch (Campaign status: `BLOCKED`).
8. **Preflight Gates**: Run campaign readiness, sufficiency, measurement readiness, and launch readiness evaluators before activation.
9. **Separate Strategy from Execution**: Maintain a strict boundary between execution variables and strategic parameters.
10. **Feedback Loop**: Record detailed performance results and learnings to feed back into strategy recommendations.

---

## Strategy vs. Execution Changes

The Campaign Execution Skill must explicitly categorize changes:

### Allowed Execution Changes
- Channel adaptation (formatting messaging for LinkedIn vs email vs ad copy)
- Asset formats (PDF vs landing page vs video scripts)
- Copy variations and headline phrasing
- CTA visual presentation and callout language
- Campaign timing, launch date updates, and scheduling
- Sequence step order and pacing

### Prohibited Strategic Changes (Requires Strategic Review)
- Redefining target ICP or customer segment parameters
- Altering core positioning or brand value proposition
- Modifying the underlying strategic goal or objective
- Changing fundamental differentiation points

> [!IMPORTANT]
> If any strategic change is required or discovered as an execution bottleneck, the skill MUST yield:
> **`STRATEGIC REVIEW REQUIRED`**
> Rather than silently updating the ICP or positioning.
