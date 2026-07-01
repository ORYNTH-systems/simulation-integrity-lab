class GoalEvaluator:

    def evaluate_graph(self, graph, goal):

        results = []

        for node in graph.nodes.values():

            result = goal.evaluate(node)

            results.append({
                "node_id": node.node_id,
                "mutation_id": node.mutation_id,
                "goal": result
            })

        return {
            "goal_id": goal.goal_id,
            "description": goal.description,
            "satisfied_count": sum(
                1
                for result in results
                if result["goal"]["satisfied"]
            ),
            "results": results
        }

    def satisfying_nodes(self, graph, goal):

        return [
            node
            for node in graph.nodes.values()
            if goal.evaluate(node)["satisfied"]
        ]
