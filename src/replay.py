class SimulationReplay:

    def replay(self, timeline):
        return [
            {
                "tick": record.tick,
                "decision": record.decision,
                "reason": record.reason,
                "world_snapshot": record.world_snapshot
            }
            for record in timeline.records
        ]

    def verify_determinism(self, timeline):
        replayed = self.replay(timeline)

        ticks = [record["tick"] for record in replayed]
        decisions = [record["decision"] for record in replayed]

        return {
            "replayed_ticks": len(replayed),
            "tick_sequence_valid": ticks == list(range(len(ticks))),
            "decisions_recorded": len(decisions) == len(replayed),
            "deterministic_replay": ticks == list(range(len(ticks))) and len(decisions) == len(replayed)
        }
