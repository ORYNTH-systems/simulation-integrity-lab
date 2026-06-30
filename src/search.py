from dataclasses import dataclass
from typing import Any


@dataclass
class SearchNode:
    node_id: str
    world: Any
    depth: int
    parent: str | None = None
    score: float = 0.0
