from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Entity:
    entity_id: str
    kind: str
    state: Dict[str, Any]
