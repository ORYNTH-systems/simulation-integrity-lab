class ConstitutionalHeuristic:

    def score(self, world):

        score = 100.0

        if not world.constraints.get("admissible", True):
            score -= 40

        if not world.safety.get("safe", True):
            score -= 30

        if not world.artifact.get("present", True):
            score -= 30

        return score
