class ConstitutionalPlanner:

    def evaluate(self, futures):

        evaluated = []

        for future in futures:

            decision = "PASS"

            if "constraint_failure" in future["id"]:
                decision = "BLOCK"

            if "safety_failure" in future["id"]:
                decision = "BLOCK"

            evaluated.append({
                "future": future["id"],
                "decision": decision
            })

        return evaluated
