class TemporalPolicy:

    def __init__(self, admissibility_window):
        self.window = admissibility_window

    def evaluate(self, world, current_time):
        if not self.window.is_open(current_time):
            world.constraints["admissible"] = False
            world.constraints["reason"] = "temporal_admissibility_window_closed"
        else:
            world.constraints["admissible"] = True
            world.constraints["reason"] = "temporal_admissibility_window_open"

        return world
