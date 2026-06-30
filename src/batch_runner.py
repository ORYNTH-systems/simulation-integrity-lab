from pathlib import Path

from world import WorldState
from scenario_runner import ScenarioRunner
from scenario_execution import ScenarioExecution
from decision_engine import ConstitutionalDecisionEngine
from decision_history import DecisionHistory
from report_writer import ReportWriter

runner = ScenarioRunner()
execution = ScenarioExecution()
decision_engine = ConstitutionalDecisionEngine()
writer = ReportWriter()

for scenario_file in sorted(Path("scenarios").glob("*.json")):

    scenario = runner.load(scenario_file.name)

    world = WorldState()

    history = DecisionHistory()

    events = {}

    for event in scenario["events"]:
        events.setdefault(event["tick"], []).append(event)

    for tick in range(scenario["ticks"]):

        world.tick = tick

        execution.execute_tick(world, tick, events)

        decision = decision_engine.evaluate(world)

        history.record(
            tick,
            decision,
            world
        )

    report = {
        "scenario_id": scenario["scenario_id"],
        "title": scenario["title"],
        "history": history.export(),
        "status": "SCENARIO_EXECUTED"
    }

    writer.write(
        f'{scenario["scenario_id"]}-report.json',
        report
    )

    print(
        f'Completed {scenario["scenario_id"]}'
    )

print()

print("Batch Complete")
