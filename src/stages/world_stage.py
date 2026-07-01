from stages.base_stage import ConstitutionalStage


class WorldStage(ConstitutionalStage):

    name = "World"

    def evaluate(self, context):

        world = context.world

        if world.constraints.get("world_blocked", False):
            return {
                "decision": "BLOCK",
                "reason": "world_constraint_blocked"
            }

        return {
            "decision": "PASS",
            "reason": "world_state_valid"
        }
