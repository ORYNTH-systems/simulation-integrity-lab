from entity_decision_engine import EntityDecisionEngine


class InteractionEngine:

    def __init__(self):
        self.entity_engine = EntityDecisionEngine()

    def evaluate(self, sender, receiver, interaction):

        sender_result = self.entity_engine.evaluate(sender)

        if sender_result["decision"] == "BLOCK":
            return sender_result

        receiver_result = self.entity_engine.evaluate(receiver)

        if receiver_result["decision"] == "BLOCK":
            return receiver_result

        return {
            "decision": "PASS",
            "reason": "interaction_constitutionally_admissible"
        }
