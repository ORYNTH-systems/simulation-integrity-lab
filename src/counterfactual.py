from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class CounterfactualState:
    state_id: str
    description: str
    world: Dict[str, Any]
