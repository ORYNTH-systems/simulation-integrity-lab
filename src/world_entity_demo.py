import json

from world import WorldState
from entity import RichEntity
from entity_decision_engine import EntityDecisionEngine

world = WorldState()

entity_a = RichEntity(
    entity_id="entity_a",
    entity_type="agent"
)

entity_b = RichEntity(
    entity_id="entity_b",
    entity_type="agent",
    resources={"available": False}
)

world.entities.add(entity_a)
world.entities.add(entity_b)

engine = EntityDecisionEngine()

decisions = {}

for entity in world.entities.all():
    decisions[entity.entity_id] = engine.evaluate(entity)

print(json.dumps({
    "world": world.snapshot(),
    "entity_decisions": decisions,
    "status": "WORLD_ENTITY_REGISTRY_ACTIVE"
}, indent=2))
