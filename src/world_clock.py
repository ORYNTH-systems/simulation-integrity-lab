class WorldClock:

    def __init__(self):
        self.current_time = 0

    def update(self, time_value):
        self.current_time = time_value
        return self.current_time
