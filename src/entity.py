from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class RichEntity:
    entity_id: str
    entity_type: str
    identity: Dict[str, Any] = field(default_factory=lambda: {"valid": True})
    authority: Dict[str, Any] = field(default_factory=lambda: {"active": True})
    intent: Dict[str, Any] = field(default_factory=lambda: {"allowed": True})
    resources: Dict[str, Any] = field(default_factory=lambda: {"available": True})
    constraints: Dict[str, Any] = field(default_factory=lambda: {"satisfied": True})
    state: Dict[str, Any] = field(default_factory=dict)
    history: List[Dict[str, Any]] = field(default_factory=list)

    def snapshot(self):
        return {
            "entity_id": self.entity_id,
            "entity_type": self.entity_type,
            "identity": self.identity,
            "authority": self.authority,
            "intent": self.intent,
            "resources": self.resources,
            "constraints": self.constraints,
            "state": self.state,
            "history_length": len(self.history)
        }
