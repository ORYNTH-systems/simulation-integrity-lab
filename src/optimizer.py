class OptimizationEngine:

    def optimize(self, evaluated):

        total = len(evaluated)

        admissible = sum(
            1
            for future in evaluated
            if future["decision"] == "PASS"
        )

        return {
            "candidate_futures": total,
            "constitutionally_admissible": admissible,
            "optimization_ratio": admissible / total if total else 0.0
        }
