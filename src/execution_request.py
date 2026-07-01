from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ExecutionRequest:
    request_id: str
    requester: str
    action: str
    target: str
    payload: Dict[str, Any]
