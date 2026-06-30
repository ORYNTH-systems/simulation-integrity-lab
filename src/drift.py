class ConstitutionalDrift:

    def compare(self, baseline, candidate):

        drift = {
            "tick_delta": candidate.tick - baseline.tick,
            "safety_changed": baseline.safety != candidate.safety,
            "constraint_changed": baseline.constraints != candidate.constraints,
            "artifact_changed": baseline.artifact != candidate.artifact
        }

        drift["constitutional_drift"] = (
            drift["safety_changed"] or
            drift["constraint_changed"] or
            drift["artifact_changed"]
        )

        drift["drift_score"] = sum([
            drift["safety_changed"],
            drift["constraint_changed"],
            drift["artifact_changed"]
        ])

        return drift
