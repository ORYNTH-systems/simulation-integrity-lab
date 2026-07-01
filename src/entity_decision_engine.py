class EntityDecisionEngine:

    def evaluate(self, entity):

        if not entity.identity.get("valid", True):
            return {
                "decision": "BLOCK",
                "reason": "entity_identity_invalid"
            }

        if not entity.authority.get("active", True):
            return {
                "decision": "BLOCK",
                "reason": "entity_authority_inactive"
            }

        if not entity.intent.get("allowed", True):
            return {
                "decision": "BLOCK",
                "reason": "entity_intent_disallowed"
            }

        if not entity.resources.get("available", True):
            return {
                "decision": "BLOCK",
                "reason": "entity_resource_unavailable"
            }

        if not entity.constraints.get("satisfied", True):
            return {
                "decision": "BLOCK",
                "reason": "entity_constraints_unsatisfied"
            }

        return {
            "decision": "PASS",
            "reason": "entity_constitutionally_admissible"
        }
