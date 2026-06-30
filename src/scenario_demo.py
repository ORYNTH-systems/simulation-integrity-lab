from world import WorldState
from scenario_runner import ScenarioRunner
from scenario_execution import ScenarioExecution

runner = ScenarioRunner()
execution = ScenarioExecution()

world = WorldState()

scenario = runner.load("SIL-001-temporal-safety.json")

events = {}

for event in scenario["events"]:
    events.setdefault(event["tick"], []).append(event)

print()

print("Scenario:", scenario["scenario_id"])
print()

for tick in range(scenario["ticks"]):

    world.tick = tick

    execution.execute_tick(world, tick, events)

    print(
        tick,
        world.safety,
        world.constraints,
        world.artifact
    )

print()

print("Scenario Complete")
