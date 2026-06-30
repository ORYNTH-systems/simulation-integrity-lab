from consensus import ConsensusEngine
from arbitration import ArbitrationEngine


class NegotiationEngine:

    def __init__(self):
        self.consensus = ConsensusEngine()
        self.arbitration = ArbitrationEngine()

    def negotiate(self, proposals):
        consensus_result = self.consensus.evaluate(proposals)

        if consensus_result["consensus"]:
            return {
                "status": "CONSENSUS",
                "decision": "PASS",
                "reason": "no_resource_conflict",
                "consensus": consensus_result
            }

        all_conflicting = []

        for proposal_ids in consensus_result["conflicts"].values():
            for proposal in proposals:
                if proposal.proposal_id in proposal_ids:
                    all_conflicting.append(proposal)

        arbitration = self.arbitration.resolve(all_conflicting)

        return {
            "status": "ARBITRATED",
            "decision": "PASS",
            "reason": "conflict_resolved_by_arbitration",
            "consensus": consensus_result,
            "arbitration": arbitration
        }
