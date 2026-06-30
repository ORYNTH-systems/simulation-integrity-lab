from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class SimulationEvent:
    tick: int
    event_type: str
    payload: Dict[str, Any]
