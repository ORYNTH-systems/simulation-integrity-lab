class ArbitrationEngine:

    def resolve(self, proposals):
        if not proposals:
            return None

        ranked = sorted(
            proposals,
            key=lambda proposal: proposal.priority,
            reverse=True
        )

        winner = ranked[0]

        return {
            "winner": winner.proposal_id,
            "proposer_id": winner.proposer_id,
            "resource_id": winner.resource_id,
            "reason": "highest_priority_proposal_selected"
        }
