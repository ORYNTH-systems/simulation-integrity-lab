class ConstitutionalPipeline:

    def __init__(self):

        self.stages = []

    def add_stage(self, stage):

        self.stages.append(stage)

    def evaluate(self, context):

        for stage in self.stages:

            result = stage.evaluate(context)

            if result["decision"] == "BLOCK":
                return result

        return {
            "decision": "PASS",
            "reason": "constitutional_pipeline_passed"
        }
