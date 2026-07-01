from stages.base_stage import ConstitutionalStage
from entity_decision_engine import EntityDecisionEngine


class IdentityStage(ConstitutionalStage):

    name = "Identity"

    def __init__(self):
        self.engine = EntityDecisionEngine()

    def evaluate(self, context):
        return self.engine.evaluate(context.requester)
