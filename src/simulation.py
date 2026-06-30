from world import WorldState
from governor import SimulationGovernor
from timeline import SimulationTimeline
from tick import TickResult
from scheduler import EventScheduler
from mutator import WorldMutator

from clock import SimulationClock
from world_clock import WorldClock
from admissibility_window import AdmissibilityWindow
from temporal_policy import TemporalPolicy


class Simulation:

    def __init__(self):
        self.world = WorldState()

        self.clock = SimulationClock()
        self.world_clock = WorldClock()

        self.temporal_policy = TemporalPolicy(
            AdmissibilityWindow(
                start_time=0,
                end_time=10
            )
        )

        self.governor = SimulationGovernor()
        self.timeline = SimulationTimeline()
        self.scheduler = EventScheduler()
        self.mutator = WorldMutator()

    def step(self):

        current_time = self.clock.time_for_tick(self.world.tick)

        self.world_clock.update(current_time)

        self.world = self.temporal_policy.evaluate(
            self.world,
            current_time
        )

        for event in self.scheduler.events_for_tick(self.world.tick):
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
