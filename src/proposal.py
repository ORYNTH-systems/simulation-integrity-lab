from dataclasses import dataclass


@dataclass
class Proposal:
    proposal_id: str
    proposer_id: str
    action: str
    resource_id: str
    priority: int = 1
