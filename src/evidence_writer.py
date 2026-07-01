import json
from pathlib import Path


class EvidenceWriter:

    def __init__(self, directory="reports/evidence"):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)

    def write(self, evidence_json):

        filename = f'{evidence_json["execution_id"]}.evidence.json'

        path = self.directory / filename

        with open(path, "w", encoding="utf-8") as f:
            json.dump(evidence_json, f, indent=4)

        return str(path)
