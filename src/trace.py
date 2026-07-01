from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class ConstitutionalTrace:

    execution_id: str

    stages: List[Dict[str, Any]] = field(
        default_factory=list
    )

    decision: str = ""

    reason: str = ""

    def add_stage(
        self,
        stage,
        decision,
        reason,
        metadata=None
    ):

        self.stages.append({

            "stage": stage,

            "decision": decision,

            "reason": reason,

            "metadata": metadata or {}

        })

    def finalize(
        self,
        decision,
        reason
    ):

        self.decision = decision
        self.reason = reason

    def to_json(self):

        return {

            "execution_id": self.execution_id,

            "decision": self.decision,

            "reason": self.reason,

            "stages": self.stages

        }
