class ConstitutionalStage:

    name = "UnnamedStage"

    def evaluate(self, context):
        raise NotImplementedError(
            f"{self.name} must implement evaluate()."
        )
