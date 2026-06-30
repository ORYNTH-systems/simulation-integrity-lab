class WorldMutator:

    def apply(self, world, event):
        if event.event_type == "safety_failure":
            world.safety["safe"] = False
            world.safety["reason"] = event.payload.get("reason")

        if event.event_type == "safety_recovery":
            world.safety["safe"] = True
            world.safety["reason"] = event.payload.get("reason")

        return world
