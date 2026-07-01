from goal import ConstitutionalGoal


class AdmissibleStateGoal(ConstitutionalGoal):

    goal_id = "admissible_state"
    description = "Find states that remain constitutionally admissible."

    def evaluate(self, node):

        return {
            "goal_id": self.goal_id,
            "satisfied": node.admissible,
            "reason": (
                "state_admissible"
                if node.admissible
                else "state_not_admissible"
            )
        }


class DelegationValidGoal(ConstitutionalGoal):

    goal_id = "delegation_valid"
    description = "Find states where delegation remains valid."

    def evaluate(self, node):

        if node.evaluation["decision"] == "PASS":
            return {
                "goal_id": self.goal_id,
                "satisfied": True,
                "reason": "delegation_valid_under_kernel"
            }

        if node.evaluation["reason"] == "delegation_invalid_or_expired":
            return {
                "goal_id": self.goal_id,
                "satisfied": False,
                "reason": "delegation_invalid_or_expired"
            }

        return {
            "goal_id": self.goal_id,
            "satisfied": False,
            "reason": "goal_not_satisfied"
        }
