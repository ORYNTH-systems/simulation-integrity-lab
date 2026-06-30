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

from agent import Agent
from authority import Authority
from intent import Intent
from resource import ResourceClaim

from proposal import Proposal
from negotiation import NegotiationEngine


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

    agent_a = Agent(
        agent_id="agent_a",
        authority=Authority(level="standard", active=True),
        intent=Intent(action="render_overlay", allowed=True),
        resource=ResourceClaim(resource_id="display_channel", available=True)
    )

    agent_b = Agent(
        agent_id="agent_b",
        authority=Authority(level="standard", active=False),
        intent=Intent(action="render_overlay", allowed=True),
        resource=ResourceClaim(resource_id="display_channel", available=True)
    )

    agent_a_decision, agent_a_reason = agent_a.evaluate()
    agent_b_decision, agent_b_reason = agent_b.evaluate()

    proposals = [
        Proposal(
            proposal_id="proposal_a",
            proposer_id="agent_a",
            action="claim_display_channel",
            resource_id="display_channel",
            priority=2
        ),
        Proposal(
            proposal_id="proposal_b",
            proposer_id="agent_b",
            action="claim_display_channel",
            resource_id="display_channel",
            priority=1
        )
    ]

    negotiation = NegotiationEngine().negotiate(proposals)

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
        "agents":{
            "agent_a":{
                "decision":agent_a_decision,
                "reason":agent_a_reason
            },
            "agent_b":{
                "decision":agent_b_decision,
                "reason":agent_b_reason
            }
        },
        "negotiation":negotiation,
        "status":"SIMULATION_INTEGRITY_ENGINE_ACTIVE"
    }

    print(json.dumps(output,indent=2))


if __name__=="__main__":
    main()
