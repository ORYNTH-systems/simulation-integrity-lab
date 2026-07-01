from dataclasses import dataclass, field
from typing import Dict, Any
from entity_registry import EntityRegistry


@dataclass
class WorldState:
    tick: int = 0
    entities: EntityRegistry = field(default_factory=EntityRegistry)
    constraints: Dict[str, Any] = field(default_factory=dict)
    safety: Dict[str, Any] = field(default_factory=lambda: {"safe": True})
    artifact: Dict[str, Any] = field(default_factory=lambda: {"present": True})

    def snapshot(self) -> Dict[str, Any]:
        return {
            "tick": self.tick,
            "entities": self.entities.snapshot(),
            "constraints": self.constraints,
            "safety": self.safety,
            "artifact": self.artifact
        }
