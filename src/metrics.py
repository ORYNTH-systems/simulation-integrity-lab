class SimulationMetrics:

    def summarize(self, timeline):
        total = len(timeline.records)
        passed = sum(1 for r in timeline.records if r.decision == "PASS")
        blocked = sum(1 for r in timeline.records if r.decision == "BLOCK")

        return {
            "total_ticks": total,
            "pass": passed,
            "block": blocked,
            "constitutional_continuity": passed == total
        }
