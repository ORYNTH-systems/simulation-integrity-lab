from dataclasses import dataclass
from authority import Authority
from intent import Intent
from resource import ResourceClaim


@dataclass
class Agent:
    agent_id: str
    authority: Authority
    intent: Intent
    resource: ResourceClaim

    def evaluate(self):
        if not self.authority.admissible():
            return "BLOCK", "authority_inactive"

        if not self.intent.admissible():
            return "BLOCK", "intent_not_allowed"

        if not self.resource.admissible():
            return "BLOCK", "resource_unavailable"

        return "PASS", "agent_constitutionally_admissible"
