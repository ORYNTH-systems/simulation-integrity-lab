from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class TickResult:
    tick: int
    admissible: bool
    safe: bool
    artifact_present: bool
    decision: str
    reason: str
    world_snapshot: Dict[str, Any]
