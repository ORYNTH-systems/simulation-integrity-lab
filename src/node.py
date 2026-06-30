from dataclasses import dataclass


@dataclass
class SimulationNode:
    node_id: str
    active: bool = True
    constitutional_hash: str = "GENESIS"

    def heartbeat(self):
        return {
            "node_id": self.node_id,
            "active": self.active,
            "constitutional_hash": self.constitutional_hash
        }
