import json
from pathlib import Path


class BenchmarkMetrics:

    def summarize(self):

        reports = sorted(Path("reports").glob("SIL-*-report.json"))

        total = 0
        passed = 0
        blocked = 0

        for report in reports:

            with open(report, "r", encoding="utf-8") as f:
                data = json.load(f)

            total += 1

            history = data["history"]

            if any(
                entry["decision"]["decision"] == "BLOCK"
                for entry in history
            ):
                blocked += 1
            else:
                passed += 1

        return {
            "benchmark": "Simulation Integrity Lab",
            "version": "v0.2",
            "scenario_count": total,
            "fully_passed": passed,
            "blocked": blocked,
            "reports": len(reports)
        }
