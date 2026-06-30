import json
import sys
from simulation import Simulation
from metrics import SimulationMetrics


def main():
    ticks = 10

    if len(sys.argv) > 1:
        ticks = int(sys.argv[1])

    sim = Simulation()
    results = sim.run(ticks)

    metrics = SimulationMetrics().summarize(sim.timeline)

    output = {
        "results": [r.__dict__ for r in results],
        "metrics": metrics,
        "status": "SIMULATION_INTEGRITY_ENGINE_ACTIVE"
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
