from stages.base_stage import ConstitutionalStage


class SafetyStage(ConstitutionalStage):

    name = "Safety"

    def evaluate(self, context):

        safety = context.world.safety

        if not safety.get("safe", True):
            return {
                "decision": "BLOCK",
                "reason": safety.get(
                    "reason",
                    "world_not_safe"
                )
            }

        return {
            "decision": "PASS",
            "reason": "safety_valid"
        }
