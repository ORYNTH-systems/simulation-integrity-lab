import json

from delegation import Delegation
from delegation_engine import DelegationEngine

engine = DelegationEngine()

valid_delegation = Delegation(
    delegation_id="del_001",
    delegator_id="agent_a",
    delegatee_id="agent_b",
    authority_scope="render_overlay",
    active=True,
    expires_at_tick=10
)

expired_delegation = Delegation(
    delegation_id="del_002",
    delegator_id="agent_a",
    delegatee_id="agent_c",
    authority_scope="render_overlay",
    active=True,
    expires_at_tick=3
)

result = {
    "tick": 5,
    "valid_delegation": engine.evaluate(valid_delegation, 5),
    "expired_delegation": engine.evaluate(expired_delegation, 5),
    "status": "AUTHORITY_DELEGATION_ACTIVE"
}

print(json.dumps(result, indent=2))
