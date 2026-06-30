import json

from simulation import Simulation
from forecast import ForecastEngine
from planner import ConstitutionalPlanner
from strategy import StrategyEngine
from optimizer import OptimizationEngine


sim = Simulation()
sim.run(5)

futures = ForecastEngine().generate(sim.world)

evaluated = ConstitutionalPlanner().evaluate(futures)

selected = StrategyEngine().select(evaluated)

optimization = OptimizationEngine().optimize(evaluated)

print(json.dumps({
    "generated_futures": futures,
    "evaluated": evaluated,
    "selected": selected,
    "optimization": optimization,
    "status": "COUNTERFACTUAL_PLANNING_ACTIVE"
}, indent=2))
