from stages.base_stage import ConstitutionalStage


class IntentStage(ConstitutionalStage):

    name = "Intent"

    def evaluate(self, context):

        intent = context.requester.intent

        if not intent.get("allowed", True):
            return {
                "decision": "BLOCK",
                "reason": "intent_disallowed"
            }

        return {
            "decision": "PASS",
            "reason": "intent_valid"
        }
