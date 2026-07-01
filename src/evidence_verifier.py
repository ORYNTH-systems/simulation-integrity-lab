from evidence_object import ConstitutionalEvidenceObject


class EvidenceVerifier:

    def verify(self, evidence_json):

        required = [
            "evidence_id",
            "execution_id",
            "decision",
            "reason",
            "trace",
            "metadata",
            "evidence_hash"
        ]

        for field in required:
            if field not in evidence_json:
                return {
                    "verified": False,
                    "reason": f"missing_{field}"
                }

        reconstructed = ConstitutionalEvidenceObject(
            evidence_id=evidence_json["evidence_id"],
            execution_id=evidence_json["execution_id"],
            decision=evidence_json["decision"],
            reason=evidence_json["reason"],
            trace=evidence_json["trace"],
            metadata=evidence_json["metadata"]
        )

        expected_hash = reconstructed.compute_hash()

        if expected_hash != evidence_json["evidence_hash"]:
            return {
                "verified": False,
                "reason": "evidence_hash_mismatch"
            }

        return {
            "verified": True,
            "reason": "evidence_hash_verified"
        }
