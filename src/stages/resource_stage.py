from stages.base_stage import ConstitutionalStage


class ResourceStage(ConstitutionalStage):

    name = "Resource"

    def evaluate(self, context):

        resources = context.requester.resources

        if not resources.get("available", True):
            return {
                "decision": "BLOCK",
                "reason": "resource_unavailable"
            }

        return {
            "decision": "PASS",
            "reason": "resource_valid"
        }
