from scenario_loader import ScenarioLoader


class ScenarioRunner:

    def __init__(self):
        self.loader = ScenarioLoader()

    def available(self):
        return [
            scenario["scenario_id"]
            for scenario in self.loader.load_all()
        ]

    def load(self, scenario_file):
        return self.loader.load(scenario_file)
