from stages.base_stage import ConstitutionalStage


class TemporalStage(ConstitutionalStage):

    name = "Temporal"

    def evaluate(self, context):

        request = context.request

        expires = request.payload.get("expires_at_tick")

        if expires is not None:

            if context.tick > expires:

                return {
                    "decision": "BLOCK",
                    "reason": "execution_window_expired"
                }

        return {
            "decision": "PASS",
            "reason": "temporal_window_valid"
        }
