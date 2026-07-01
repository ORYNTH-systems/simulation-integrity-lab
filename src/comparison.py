class ConstitutionalComparator:

    def compare(self, baseline, counterfactual):

        baseline_decision = baseline["decision"]
        counterfactual_decision = counterfactual["decision"]

        comparison = {
            "baseline_decision": baseline_decision,
            "counterfactual_decision": counterfactual_decision,
            "changed": baseline_decision != counterfactual_decision,
            "first_divergence": None
        }

        baseline_stages = {
            stage["stage"]: stage
            for stage in baseline.get("stages", [])
        }

        counterfactual_stages = {
            stage["stage"]: stage
            for stage in counterfactual.get("stages", [])
        }

        for stage_name, baseline_stage in baseline_stages.items():

            counterfactual_stage = counterfactual_stages.get(stage_name)

            if counterfactual_stage is None:

                comparison["first_divergence"] = {
                    "stage": stage_name,
                    "baseline": baseline_stage["decision"],
                    "counterfactual": "MISSING",
                    "reason": "stage_missing_in_counterfactual"
                }

                return comparison

            if baseline_stage["decision"] != counterfactual_stage["decision"]:

                comparison["first_divergence"] = {
                    "stage": stage_name,
                    "baseline": baseline_stage["decision"],
                    "counterfactual": counterfactual_stage["decision"],
                    "reason": counterfactual_stage["reason"]
                }

                return comparison

        return comparison
