class ConstitutionalGoal:

    goal_id = "base_goal"
    description = "Base constitutional goal."

    def evaluate(self, node):
        raise NotImplementedError(
            f"{self.goal_id} must implement evaluate()."
        )
