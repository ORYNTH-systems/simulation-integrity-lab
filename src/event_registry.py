class EventRegistry:

    def __init__(self):
        self.handlers = {
            "safety_failure": self.handle_safety_failure,
            "safety_recovery": self.handle_safety_recovery,
            "constraint_revocation": self.handle_constraint_revocation,
            "constraint_recovery": self.handle_constraint_recovery,
            "artifact_loss": self.handle_artifact_loss,
            "artifact_recovery": self.handle_artifact_recovery
        }

    def apply(self, world, event):
        handler = self.handlers.get(event.event_type)

        if handler is None:
            world.constraints["admissible"] = False
            world.constraints["reason"] = "unknown_event_type"
            return world

        return handler(world, event)

    def handle_safety_failure(self, world, event):
        world.safety["safe"] = False
        world.safety["reason"] = event.payload.get("reason", "safety_failure")
        return world

    def handle_safety_recovery(self, world, event):
        world.safety["safe"] = True
        world.safety["reason"] = event.payload.get("reason", "safety_recovery")
        return world

    def handle_constraint_revocation(self, world, event):
        world.constraints["admissible"] = False
        world.constraints["reason"] = event.payload.get("reason", "constraint_revoked")
        return world

    def handle_constraint_recovery(self, world, event):
        world.constraints["admissible"] = True
        world.constraints["reason"] = event.payload.get("reason", "constraint_recovered")
        return world

    def handle_artifact_loss(self, world, event):
        world.artifact["present"] = False
        world.artifact["reason"] = event.payload.get("reason", "artifact_lost")
        return world

    def handle_artifact_recovery(self, world, event):
        world.artifact["present"] = True
        world.artifact["reason"] = event.payload.get("reason", "artifact_recovered")
        return world
