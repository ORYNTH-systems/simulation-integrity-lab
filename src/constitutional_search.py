from counterfactual import CounterfactualEngine


class ConstitutionalSearch:

    def __init__(self):

        self.counterfactual_engine = CounterfactualEngine()

    def search(self, kernel, context, candidates):

        results = []

        for candidate in candidates:

            evaluation = self.counterfactual_engine.evaluate(
                kernel,
                context,
                candidate["mutator"]
            )

            results.append({
                "candidate_id": candidate["candidate_id"],
                "description": candidate["description"],
                "evaluation": evaluation,
                "admissible": evaluation["decision"] == "PASS"
            })

        return {
            "candidate_count": len(results),
            "admissible_count": sum(
                1
                for result in results
                if result["admissible"]
            ),
            "results": results
        }
