import json

from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_engine import ConstitutionalExecutionEngine

entity = RichEntity(
    entity_id="robot_001",
    entity_type="robot"
)

delegation = Delegation(
    delegation_id="del_001",
    delegator_id="controller",
    delegatee_id="robot_001",
    authority_scope="deliver",
    expires_at_tick=20
)

request = ExecutionRequest(
    request_id="req_001",
    requester="robot_001",
    action="deliver_package",
    target="warehouse_A",
    payload={}
)

engine = ConstitutionalExecutionEngine()

result = engine.evaluate(
    entity,
    delegation,
    request,
    tick=5
)

print(json.dumps(result, indent=2))
