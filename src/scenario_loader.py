import json
from pathlib import Path


class ScenarioLoader:

    def __init__(self, scenario_directory="scenarios"):
        self.scenario_directory = Path(scenario_directory)

    def load(self, filename):

        path = self.scenario_directory / filename

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_all(self):

        scenarios = []

        for file in sorted(self.scenario_directory.glob("*.json")):
            scenarios.append(self.load(file.name))

        return scenarios
