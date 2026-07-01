import json

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_context import ExecutionContext

from kernel import ConstitutionalKernel
from constitutional_search import ConstitutionalSearch

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
    request_id="search-001",
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

candidates = [
    {
        "candidate_id": "keep_current_delegation",
        "description": "Preserve current delegation state",
        "mutator": lambda c: c
    },
    {
        "candidate_id": "expire_delegation",
        "description": "Force delegation expiration",
        "mutator": lambda c: setattr(
            c.delegation,
            "expires_at_tick",
            0
        )
    },
    {
        "candidate_id": "revoke_authority",
        "description": "Deactivate requester authority",
        "mutator": lambda c: c.requester.authority.update({
            "active": False
        })
    }
]

result = ConstitutionalSearch().search(
    kernel,
    context,
    candidates
)

print(json.dumps(result, indent=4))
