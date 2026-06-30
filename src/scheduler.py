from events import SimulationEvent


class EventScheduler:

    def __init__(self):
        self.events = [
            SimulationEvent(
                tick=3,
                event_type="safety_failure",
                payload={"reason": "scheduled_safety_failure"}
            ),
            SimulationEvent(
                tick=6,
                event_type="safety_recovery",
                payload={"reason": "scheduled_safety_recovery"}
            ),
            SimulationEvent(
                tick=8,
                event_type="constraint_revocation",
                payload={"reason": "scheduled_constraint_revocation"}
            ),
            SimulationEvent(
                tick=10,
                event_type="constraint_recovery",
                payload={"reason": "scheduled_constraint_recovery"}
            ),
            SimulationEvent(
                tick=12,
                event_type="artifact_loss",
                payload={"reason": "scheduled_artifact_loss"}
            ),
            SimulationEvent(
                tick=14,
                event_type="artifact_recovery",
                payload={"reason": "scheduled_artifact_recovery"}
            )
        ]

    def events_for_tick(self, tick):
        return [event for event in self.events if event.tick == tick]
