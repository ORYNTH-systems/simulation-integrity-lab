class DecisionHistory:

    def __init__(self):
        self.records = []

    def record(self, tick, decision, world):

        self.records.append({
            "tick": tick,
            "decision": decision,
            "snapshot": world.snapshot()
        })

    def export(self):
        return self.records
