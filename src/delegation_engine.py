class DelegationEngine:

    def evaluate(self, delegation, tick):

        if not delegation.valid_at(tick):
            return {
                "decision": "BLOCK",
                "reason": "delegation_invalid_or_expired"
            }

        return {
            "decision": "PASS",
            "reason": "delegation_constitutionally_valid"
        }
