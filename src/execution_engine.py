from delegation_engine import DelegationEngine
from entity_decision_engine import EntityDecisionEngine


class ConstitutionalExecutionEngine:

    def __init__(self):

        self.entity_engine = EntityDecisionEngine()
        self.delegation_engine = DelegationEngine()

    def evaluate(self, context):

        entity = self.entity_engine.evaluate(context.requester)

        if entity["decision"] == "BLOCK":
            return entity

        delegated = self.delegation_engine.evaluate(
            context.delegation,
            context.tick
        )

        if delegated["decision"] == "BLOCK":
            return delegated

        return {
            "decision": "PASS",
            "reason": "execution_constitutionally_admissible",
            "action": context.request.action,
            "request_id": context.request.request_id,
            "requester": context.requester.entity_id,
            "tick": context.tick
        }
