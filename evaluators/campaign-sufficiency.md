# Campaign Sufficiency Evaluator

Evaluates whether the Execution Agent has sufficient strategic input to safely construct the campaign.

## Inputs Evaluation Checklist
- **Objective**: Defined and aligned? (Yes/No)
- **ICP**: Defined and structured? (Yes/No)
- **Positioning**: Approved positioning reference provided? (Yes/No)
- **Messaging**: Core messaging framework present? (Yes/No)

## Execution Parameters Checklist
- **Channel**: Recommended or explicitly set? (Yes/No)
- **CTA**: Defined and measurable? (Yes/No)
- **Measurement**: Target, baseline, metrics set? (Yes/No)

## Result Output Logic
- **SUFFICIENT**: All Inputs are "Yes", and all Execution parameters are configured.
- **PARTIAL**: Inputs are "Yes" but execution parameters (like measurement metrics or landing page destinations) are incomplete. Action: Transition to DRAFT state, do not allow QA.
- **BLOCKED**: One or more Inputs (Objective, ICP, Positioning, Messaging) are "No" or missing. The Execution Agent is blocked from proceeding. DO NOT fill gaps with hallucinated assumptions.
