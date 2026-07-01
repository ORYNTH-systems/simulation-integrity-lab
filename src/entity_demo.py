import json

from entity import RichEntity
from entity_decision_engine import EntityDecisionEngine

engine = EntityDecisionEngine()

entity_a = RichEntity(
    entity_id="entity_a",
    entity_type="agent"
)

entity_b = RichEntity(
    entity_id="entity_b",
    entity_type="agent",
    authority={"active": False}
)

result = {
    "entity_a": {
        "snapshot": entity_a.snapshot(),
        "decision": engine.evaluate(entity_a)
    },
    "entity_b": {
        "snapshot": entity_b.snapshot(),
        "decision": engine.evaluate(entity_b)
    },
    "status": "RICH_ENTITY_MODEL_ACTIVE"
}

print(json.dumps(result, indent=2))
