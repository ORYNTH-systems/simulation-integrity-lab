import json

from entity import RichEntity
from interaction import Interaction
from interaction_engine import InteractionEngine

sender = RichEntity(
    entity_id="robot_001",
    entity_type="robot"
)

receiver = RichEntity(
    entity_id="station_001",
    entity_type="charging_station"
)

interaction = Interaction(
    sender="robot_001",
    receiver="station_001",
    action="request_charge",
    payload={}
)

engine = InteractionEngine()

result = engine.evaluate(
    sender,
    receiver,
    interaction
)

print(json.dumps(result, indent=4))
