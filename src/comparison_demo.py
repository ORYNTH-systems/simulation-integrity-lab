import json

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_context import ExecutionContext

from kernel import ConstitutionalKernel
from counterfactual import CounterfactualEngine
from comparison import ConstitutionalComparator

world = WorldState()

entity = RichEntity(
    entity_id="robot",
    entity_type="robot"
)

delegation = Delegation(
    delegation_id="del",
    delegator_id="controller",
    delegatee_id="robot",
    authority_scope="execute",
    expires_at_tick=10
)

request = ExecutionRequest(
    request_id="compare-001",
    requester="robot",
    action="move",
    target="zoneA",
    payload={}
)

context = ExecutionContext(
    world,
    entity,
    delegation,
    request,
    tick=5
)

kernel = ConstitutionalKernel()
counterfactual_engine = CounterfactualEngine()
comparator = ConstitutionalComparator()

baseline = kernel.evaluate(context)

counterfactual = counterfactual_engine.evaluate(
    kernel,
    context,
    lambda c: setattr(
        c.delegation,
        "expires_at_tick",
        0
    )
)

comparison = comparator.compare(
    baseline,
    counterfactual
)

print(json.dumps({
    "baseline": baseline,
    "counterfactual": counterfactual,
    "comparison": comparison,
    "status": "CONSTITUTIONAL_COMPARISON_ACTIVE"
}, indent=4))
