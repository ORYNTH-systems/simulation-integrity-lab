from dataclasses import dataclass

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest


@dataclass
class ExecutionContext:

    world: WorldState

    requester: RichEntity

    delegation: Delegation

    request: ExecutionRequest

    tick: int
