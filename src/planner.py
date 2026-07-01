from state_explorer import StateExplorer
from goal_evaluator import GoalEvaluator


class ConstitutionalPlanner:

    def __init__(self):

        self.explorer = StateExplorer()
        self.goal_evaluator = GoalEvaluator()

    def plan(self, graph, goal):

        satisfying_nodes = self.goal_evaluator.satisfying_nodes(
            graph,
            goal
        )

        admissible_goal_nodes = [
            node
            for node in satisfying_nodes
            if node.admissible
        ]

        if not admissible_goal_nodes:
            return {
                "plan_found": False,
                "reason": "no_admissible_goal_state"
            }

        selected = admissible_goal_nodes[0]

        return {
            "plan_found": True,
            "selected_node": selected.node_id,
            "mutation_id": selected.mutation_id,
            "path": self.explorer.path_to_root(
                graph,
                selected.node_id
            ),
            "reason": "admissible_goal_state_found"
        }
