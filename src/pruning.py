class ConstitutionalPruner:

    def admissible(self, world):

        return (
            world.constraints.get("admissible", True)
            and world.safety.get("safe", True)
            and world.artifact.get("present", True)
        )
