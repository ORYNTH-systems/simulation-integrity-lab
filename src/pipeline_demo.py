import json

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_context import ExecutionContext

from pipeline import ConstitutionalPipeline

from stages.identity_stage import IdentityStage
from stages.delegation_stage import DelegationStage

pipeline = ConstitutionalPipeline()

pipeline.add_stage(
    IdentityStage()
)

pipeline.add_stage(
    DelegationStage()
)

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
    request_id="req",
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

print(
    json.dumps(
        pipeline.evaluate(context),
        indent=4
    )
)
