from entity import RichEntity


class WorldMutationEngine:

    def apply(self, world, event):

        event_type = event["event_type"]
        payload = event.get("payload", {})
        reason = payload.get("reason", event_type)

        if event_type == "safety_failure":
            world.safety["safe"] = False
            world.safety["reason"] = reason

        elif event_type == "safety_recovery":
            world.safety["safe"] = True
            world.safety["reason"] = reason

        elif event_type == "constraint_revocation":
            world.constraints["admissible"] = False
            world.constraints["reason"] = reason

        elif event_type == "constraint_recovery":
            world.constraints["admissible"] = True
            world.constraints["reason"] = reason

        elif event_type == "artifact_loss":
            world.artifact["present"] = False
            world.artifact["reason"] = reason

        elif event_type == "artifact_recovery":
            world.artifact["present"] = True
            world.artifact["reason"] = reason

        elif event_type == "entity_spawn":
            entity = RichEntity(
                entity_id=payload["entity_id"],
                entity_type=payload.get("entity_type", "agent")
            )
            world.entities.add(entity)

        elif event_type == "entity_authority_revoked":
            entity = world.entities.get(payload["entity_id"])
            if entity:
                entity.authority["active"] = False
                entity.authority["reason"] = reason

        elif event_type == "entity_resource_loss":
            entity = world.entities.get(payload["entity_id"])
            if entity:
                entity.resources["available"] = False
                entity.resources["reason"] = reason

        else:
            world.constraints["admissible"] = False
            world.constraints["reason"] = "unknown_event_type"

        return world
