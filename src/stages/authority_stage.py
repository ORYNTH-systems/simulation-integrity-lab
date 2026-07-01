class AuthorityStage:

    def evaluate(self, context):

        authority = context.requester.authority

        if not authority.get("active", True):
            return {
                "decision": "BLOCK",
                "reason": "authority_inactive"
            }

        return {
            "decision": "PASS",
            "reason": "authority_valid"
        }
