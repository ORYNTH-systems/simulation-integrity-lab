class SimulationClock:

    def __init__(self, tick_duration=1):
        self.tick_duration = tick_duration

    def time_for_tick(self, tick):
        return tick * self.tick_duration
