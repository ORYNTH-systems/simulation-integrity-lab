import json
from pathlib import Path


class ReportWriter:

    def write(self, filename, report):

        Path("reports").mkdir(exist_ok=True)

        with open(
            Path("reports") / filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(report, f, indent=4)
