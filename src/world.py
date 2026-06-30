from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class WorldState:
    tick: int = 0
    entities: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    constraints: Dict[str, Any] = field(default_factory=dict)
    safety: Dict[str, Any] = field(default_factory=lambda: {"safe": True})
    artifact: Dict[str, Any] = field(default_factory=lambda: {"present": True})

    def snapshot(self) -> Dict[str, Any]:
        return {
            "tick": self.tick,
            "entities": self.entities,
            "constraints": self.constraints,
            "safety": self.safety,
            "artifact": self.artifact
        }
