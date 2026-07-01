class ConstitutionalMutation:

    mutation_id = "base_mutation"
    description = "Base constitutional mutation."

    def apply(self, context):
        raise NotImplementedError(
            f"{self.mutation_id} must implement apply()."
        )

    def candidate(self):
        return {
            "candidate_id": self.mutation_id,
            "description": self.description,
            "mutator": self.apply
        }
