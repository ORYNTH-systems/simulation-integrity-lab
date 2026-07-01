import time

from trace import ConstitutionalTrace


class ConstitutionalPipeline:

    def __init__(self):

        self.stages = []

    def add_stage(self, stage):

        self.stages.append(stage)

    def evaluate(self, context):

        trace = ConstitutionalTrace(
            execution_id=context.request.request_id
        )

        for stage in self.stages:

            started = time.perf_counter()

            result = stage.evaluate(context)

            elapsed_ms = round(
                (time.perf_counter() - started) * 1000,
                3
            )

            trace.add_stage(

                stage=stage.name,

                decision=result["decision"],

                reason=result["reason"],

                metadata={
                    "elapsed_ms": elapsed_ms
                }

            )

            if result["decision"] == "BLOCK":

                trace.finalize(
                    "BLOCK",
                    result["reason"]
                )

                return trace.to_json()

        trace.finalize(
            "PASS",
            "constitutional_pipeline_passed"
        )

        return trace.to_json()
