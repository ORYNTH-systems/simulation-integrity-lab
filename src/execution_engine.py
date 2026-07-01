from delegation_engine import DelegationEngine
from entity_decision_engine import EntityDecisionEngine


class ConstitutionalExecutionEngine:

    def __init__(self):

        self.entity_engine = EntityDecisionEngine()
        self.delegation_engine = DelegationEngine()

    def evaluate(
        self,
        requester,
        delegation,
        request,
        tick
    ):

        entity = self.entity_engine.evaluate(requester)

        if entity["decision"] == "BLOCK":
            return entity

        delegated = self.delegation_engine.evaluate(
            delegation,
            tick
        )

        if delegated["decision"] == "BLOCK":
            return delegated

        return {
            "decision": "PASS",
            "reason": "execution_constitutionally_admissible",
            "action": request.action
        }
