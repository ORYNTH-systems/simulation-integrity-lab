class OptimizationStrategy:

    strategy_id = "base_strategy"
    description = "Base optimization strategy."

    def score(self, graph, node):
        raise NotImplementedError(
            f"{self.strategy_id} must implement score()."
        )


class ShortestPathStrategy(OptimizationStrategy):

    strategy_id = "shortest_path"
    description = "Prefer the goal state with the shortest path from root."

    def score(self, graph, node):

        depth_score = node.depth

        return depth_score


class ConstitutionalOptimizer:

    def optimize(self, graph, candidate_nodes, strategy):

        if not candidate_nodes:
            return {
                "optimized": False,
                "reason": "no_candidate_nodes"
            }

        scored = []

        for node in candidate_nodes:

            scored.append({
                "node": node,
                "score": strategy.score(
                    graph,
                    node
                )
            })

        selected = sorted(
            scored,
            key=lambda item: item["score"]
        )[0]

        node = selected["node"]

        return {
            "optimized": True,
            "strategy": strategy.strategy_id,
            "selected_node": node.node_id,
            "mutation_id": node.mutation_id,
            "score": selected["score"],
            "reason": "optimal_constitutional_state_selected"
        }
