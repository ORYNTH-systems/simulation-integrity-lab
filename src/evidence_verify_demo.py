import json

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_context import ExecutionContext
from kernel import ConstitutionalKernel
from evidence_factory import EvidenceFactory
from evidence_verifier import EvidenceVerifier

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
    request_id="req-evidence-verify-001",
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

evidence = EvidenceFactory().from_trace(trace).to_json()

verification = EvidenceVerifier().verify(evidence)

print(json.dumps({
    "evidence": evidence,
    "verification": verification
}, indent=4))
