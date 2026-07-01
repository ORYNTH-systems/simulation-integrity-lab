import uuid

from evidence_object import ConstitutionalEvidenceObject


class EvidenceFactory:

    def from_trace(self, trace_json):

        return ConstitutionalEvidenceObject(
            evidence_id=str(uuid.uuid4()),
            execution_id=trace_json["execution_id"],
            decision=trace_json["decision"],
            reason=trace_json["reason"],
            trace=trace_json["stages"],
            metadata={
                "schema": "ORYNTH_CONSTITUTIONAL_EVIDENCE_OBJECT",
                "version": "0.1"
            }
        )
