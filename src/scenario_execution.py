from mutation_engine import WorldMutationEngine


class ScenarioExecution:

    def __init__(self):

        self.mutator = WorldMutationEngine()

    def execute_tick(self, world, tick, events):

        if tick not in events:
            return world

        for event in events[tick]:
            self.mutator.apply(world, event)

        return world
