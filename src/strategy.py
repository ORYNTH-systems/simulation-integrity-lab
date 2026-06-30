class StrategyEngine:

    def select(self, evaluated):

        admissible = [
            future
            for future in evaluated
            if future["decision"] == "PASS"
        ]

        return admissible[0] if admissible else None
