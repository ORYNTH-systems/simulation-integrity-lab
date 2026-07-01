import json

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_context import ExecutionContext
from kernel import ConstitutionalKernel
from evidence_factory import EvidenceFactory

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
    request_id="req-evidence-001",
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

trace = ConstitutionalKernel().evaluate(context)

evidence = EvidenceFactory().from_trace(trace)

print(json.dumps(evidence.to_json(), indent=4))
