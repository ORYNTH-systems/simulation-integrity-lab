from scenario_runner import ScenarioRunner


class ScenarioExecution:

    def __init__(self):
        self.runner = ScenarioRunner()

    def event_map(self, scenario):

        events = {}

        for event in scenario.get("events", []):
            events.setdefault(event["tick"], []).append(event)

        return events
