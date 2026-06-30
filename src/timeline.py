from tick import TickResult


class SimulationTimeline:

    def __init__(self):
        self.records = []

    def append(self, result: TickResult):
        self.records.append(result)

    def latest(self):
        if not self.records:
            return None
        return self.records[-1]

    def replay(self):
        return self.records
