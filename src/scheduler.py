from events import SimulationEvent


class EventScheduler:

    def __init__(self):
        self.events = [
            SimulationEvent(
                tick=3,
                event_type="safety_failure",
                payload={"safe": False, "reason": "scheduled_safety_failure"}
            ),
            SimulationEvent(
                tick=6,
                event_type="safety_recovery",
                payload={"safe": True, "reason": "scheduled_safety_recovery"}
            )
        ]

    def events_for_tick(self, tick):
        return [event for event in self.events if event.tick == tick]
