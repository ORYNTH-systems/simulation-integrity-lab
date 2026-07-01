import json

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_context import ExecutionContext

from kernel import ConstitutionalKernel
from constitutional_search import ConstitutionalSearch
from mutation_library import MutationLibrary

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
    request_id="mutation-search-001",
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

candidates = MutationLibrary().candidates()

result = ConstitutionalSearch().search(
    kernel,
    context,
    candidates
)

print(json.dumps(result, indent=4))
