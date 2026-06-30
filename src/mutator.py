from event_registry import EventRegistry


class WorldMutator:

    def __init__(self):
        self.registry = EventRegistry()

    def apply(self, world, event):
        return self.registry.apply(world, event)
