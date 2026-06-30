from scenario_runner import ScenarioRunner
from scenario_execution import ScenarioExecution


runner = ScenarioRunner()

scenario = runner.load("SIL-001-temporal-safety.json")

print()

print("Scenario:", scenario["scenario_id"])
print("Title:", scenario["title"])

print()

execution = ScenarioExecution()

events = execution.event_map(scenario)

for tick in range(scenario["ticks"]):

    print(f"Tick {tick}")

    if tick in events:

        for event in events[tick]:

            print(
                "   EVENT:",
                event["event_type"],
                event["payload"]["reason"]
            )

print()

print("Scenario Complete")
