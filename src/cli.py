import json
import sys

from simulation import Simulation
from metrics import SimulationMetrics
from replay import SimulationReplay
from branch import SimulationBranchManager


def main():

    ticks = 10

    if len(sys.argv) > 1:
        ticks = int(sys.argv[1])

    sim = Simulation()

    results = sim.run(ticks)

    metrics = SimulationMetrics().summarize(sim.timeline)

    replay = SimulationReplay().verify_determinism(sim.timeline)

    manager = SimulationBranchManager()

    baseline = manager.create_branch(sim.world, "baseline")

    alternate = manager.create_branch(sim.world, "alternate")

    comparison = manager.compare(baseline, alternate)

    output = {
        "results":[r.__dict__ for r in results],
        "metrics":metrics,
        "replay":replay,
        "branches":{
            "count":2,
            "names":manager.list_branches([baseline,alternate]),
            "comparison":comparison
        },
        "status":"SIMULATION_INTEGRITY_ENGINE_ACTIVE"
    }

    print(json.dumps(output,indent=2))


if __name__=="__main__":
    main()
