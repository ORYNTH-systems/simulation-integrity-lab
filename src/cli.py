import json
import sys

from simulation import Simulation
from metrics import SimulationMetrics
from replay import SimulationReplay
from branch import SimulationBranchManager
from drift import ConstitutionalDrift
from events import SimulationEvent
from mutator import WorldMutator
from governor import SimulationGovernor


def main():

    ticks = 16

    if len(sys.argv) > 1:
        ticks = int(sys.argv[1])

    sim = Simulation()
    results = sim.run(ticks)

    metrics = SimulationMetrics().summarize(sim.timeline)
    replay = SimulationReplay().verify_determinism(sim.timeline)

    manager = SimulationBranchManager()
    mutator = WorldMutator()
    governor = SimulationGovernor()

    baseline = manager.create_branch(sim.world, "baseline")
    alternate = manager.create_branch(sim.world, "alternate")

    divergence_event = SimulationEvent(
        tick=sim.world.tick,
        event_type="safety_failure",
        payload={"reason": "branch_divergence_safety_failure"}
    )

    alternate["world"] = mutator.apply(alternate["world"], divergence_event)

    baseline_decision, baseline_reason = governor.evaluate(baseline["world"])
    alternate_decision, alternate_reason = governor.evaluate(alternate["world"])

    drift = ConstitutionalDrift().compare(
        baseline["world"],
        alternate["world"]
    )

    output = {
        "results":[r.__dict__ for r in results],
        "metrics":metrics,
        "replay":replay,
        "branches":{
            "count":2,
            "names":manager.list_branches([baseline,alternate]),
            "baseline_decision":baseline_decision,
            "baseline_reason":baseline_reason,
            "alternate_decision":alternate_decision,
            "alternate_reason":alternate_reason
        },
        "drift":drift,
        "status":"SIMULATION_INTEGRITY_ENGINE_ACTIVE"
    }

    print(json.dumps(output,indent=2))


if __name__=="__main__":
    main()
