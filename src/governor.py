class SimulationGovernor:

    def evaluate(self, world):
        admissible = world.constraints.get("admissible", True)
        safe = world.safety.get("safe", True)
        artifact_present = world.artifact.get("present", True)

        if not admissible:
            return "BLOCK", "constraint_not_admissible"

        if not safe:
            return "BLOCK", "safety_predicate_failed"

        if not artifact_present:
            return "BLOCK", "render_authorization_artifact_missing"

        return "PASS", "constitutional_state_preserved"
