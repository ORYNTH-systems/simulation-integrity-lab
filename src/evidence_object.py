from dataclasses import dataclass, field
from typing import Dict, Any, List
import json
import hashlib


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

    evidence_hash: str = ""

    def compute_hash(self):

        payload = {
            "evidence_id": self.evidence_id,
            "execution_id": self.execution_id,
            "decision": self.decision,
            "reason": self.reason,
            "trace": self.trace,
            "metadata": self.metadata
        }

        canonical = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":")
        )

        self.evidence_hash = hashlib.sha256(
            canonical.encode("utf-8")
        ).hexdigest()

        return self.evidence_hash

    def to_json(self):

        if not self.evidence_hash:
            self.compute_hash()

        return {
            "evidence_id": self.evidence_id,
            "execution_id": self.execution_id,
            "decision": self.decision,
            "reason": self.reason,
            "trace": self.trace,
            "metadata": self.metadata,
            "evidence_hash": self.evidence_hash
        }
