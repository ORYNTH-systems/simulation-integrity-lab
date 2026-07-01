from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class ConstitutionalEvidenceObject:

    evidence_id: str

    execution_id: str

    decision: str

    reason: str

    trace: List[Dict[str, Any]]

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    def to_json(self):

        return {
            "evidence_id": self.evidence_id,
            "execution_id": self.execution_id,
            "decision": self.decision,
            "reason": self.reason,
            "trace": self.trace,
            "metadata": self.metadata
        }
