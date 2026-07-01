from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class StateNode:

    node_id: str

    parent_id: str | None

    mutation_id: str

    evaluation: Dict[str, Any]

    admissible: bool

    depth: int = 0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )
