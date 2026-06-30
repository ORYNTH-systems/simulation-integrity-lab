from world import WorldState
from governor import SimulationGovernor
from timeline import SimulationTimeline
from tick import TickResult
from scheduler import EventScheduler
from mutator import WorldMutator


class Simulation:

    def __init__(self):
        self.world = WorldState()
        self.governor = SimulationGovernor()
        self.timeline = SimulationTimeline()
        self.scheduler = EventScheduler()
        self.mutator = WorldMutator()

    def step(self):
        scheduled_events = self.scheduler.events_for_tick(self.world.tick)

        for event in scheduled_events:
            self.world = self.mutator.apply(self.world, event)

        decision, reason = self.governor.evaluate(self.world)

        result = TickResult(
            tick=self.world.tick,
            admissible=self.world.constraints.get("admissible", True),
            safe=self.world.safety.get("safe", True),
            artifact_present=self.world.artifact.get("present", True),
            decision=decision,
            reason=reason,
            world_snapshot=self.world.snapshot()
        )

        self.timeline.append(result)
        self.world.tick += 1

        return result

    def run(self, ticks=10):
        return [self.step() for _ in range(ticks)]
