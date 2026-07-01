from stages.base_stage import ConstitutionalStage
from delegation_engine import DelegationEngine


class DelegationStage(ConstitutionalStage):

    name = "Delegation"

    def __init__(self):
        self.engine = DelegationEngine()

    def evaluate(self, context):
        return self.engine.evaluate(
            context.delegation,
            context.tick
        )
