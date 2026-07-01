from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class EvidenceRecord:

    stage: str

    decision: str

    reason: str

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    rule_id: str = ""

    invariant_id: str = ""

    evidence_id: str = ""
