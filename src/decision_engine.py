class ConstitutionalDecisionEngine:

    def evaluate(self, world):

        if not world.safety.get("safe", True):
            return {
                "decision": "BLOCK",
                "reason": world.safety.get("reason", "safety_failure")
            }

        if not world.constraints.get("admissible", True):
            return {
                "decision": "BLOCK",
                "reason": world.constraints.get("reason", "constraint_failure")
            }

        if not world.artifact.get("present", True):
            return {
                "decision": "BLOCK",
                "reason": world.artifact.get("reason", "artifact_missing")
            }

        return {
            "decision": "PASS",
            "reason": "constitutional_state_preserved"
        }
