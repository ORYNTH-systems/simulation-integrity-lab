class AdmissibilityWindow:

    def __init__(self, start_time=0, end_time=10):
        self.start_time = start_time
        self.end_time = end_time

    def is_open(self, current_time):
        return self.start_time <= current_time <= self.end_time
