class ConsensusEngine:

    def evaluate(self, proposals):
        resources = {}

        for proposal in proposals:
            if proposal.resource_id not in resources:
                resources[proposal.resource_id] = []

            resources[proposal.resource_id].append(proposal)

        conflicts = {
            resource: claims
            for resource, claims in resources.items()
            if len(claims) > 1
        }

        return {
            "consensus": len(conflicts) == 0,
            "conflicts": {
                resource: [p.proposal_id for p in claims]
                for resource, claims in conflicts.items()
            }
        }
