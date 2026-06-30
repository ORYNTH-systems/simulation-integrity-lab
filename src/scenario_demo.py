from world import WorldState
from scenario_runner import ScenarioRunner
from scenario_execution import ScenarioExecution
from decision_engine import ConstitutionalDecisionEngine
from decision_history import DecisionHistory
from report_writer import ReportWriter

runner = ScenarioRunner()
execution = ScenarioExecution()
decision_engine = ConstitutionalDecisionEngine()
history = DecisionHistory()
writer = ReportWriter()

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

    decision = decision_engine.evaluate(world)

    history.record(tick, decision, world)

    print(
        "Tick",
        tick,
        "Decision:",
        decision["decision"],
        "Reason:",
        decision["reason"]
    )

report = {
    "scenario_id": scenario["scenario_id"],
    "title": scenario["title"],
    "history": history.export(),
    "status": "SCENARIO_EXECUTED"
}

writer.write("SIL-001-report.json", report)

print()
print("Scenario Complete")
print("Report written: reports/SIL-001-report.json")
