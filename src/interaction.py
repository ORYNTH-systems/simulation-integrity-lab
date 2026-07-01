from dataclasses import dataclass


@dataclass
class Interaction:
    sender: str
    receiver: str
    action: str
    payload: dict
