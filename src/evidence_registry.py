import json
from pathlib import Path
from datetime import datetime, timezone


class EvidenceRegistry:

    def __init__(self, registry_path="reports/evidence/registry.json"):

        self.registry_path = Path(registry_path)
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.registry_path.exists():
            self._write([])

    def _read(self):

        with open(self.registry_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, entries):

        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=4)

    def register(self, evidence_json, path):

        entries = self._read()

        entry = {
            "execution_id": evidence_json["execution_id"],
            "evidence_id": evidence_json["evidence_id"],
            "decision": evidence_json["decision"],
            "reason": evidence_json["reason"],
            "evidence_hash": evidence_json["evidence_hash"],
            "path": path,
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        entries.append(entry)

        self._write(entries)

        return entry

    def all(self):
        return self._read()

    def find_by_execution_id(self, execution_id):

        return [
            entry
            for entry in self._read()
            if entry["execution_id"] == execution_id
        ]

    def find_by_hash(self, evidence_hash):

        return [
            entry
            for entry in self._read()
            if entry["evidence_hash"] == evidence_hash
        ]
