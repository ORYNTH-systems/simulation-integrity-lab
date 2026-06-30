from world import WorldState
from governor import SimulationGovernor
from timeline import SimulationTimeline
from tick import TickResult


class Simulation:

    def __init__(self):
        self.world = WorldState()
        self.governor = SimulationGovernor()
        self.timeline = SimulationTimeline()

    def step(self):
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
