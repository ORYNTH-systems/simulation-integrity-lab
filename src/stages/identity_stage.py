from entity_decision_engine import EntityDecisionEngine


class IdentityStage:

    def __init__(self):

        self.engine = EntityDecisionEngine()

    def evaluate(self, context):

        return self.engine.evaluate(
            context.requester
        )
