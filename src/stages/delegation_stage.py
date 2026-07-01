from delegation_engine import DelegationEngine


class DelegationStage:

    def __init__(self):

        self.engine = DelegationEngine()

    def evaluate(self, context):

        return self.engine.evaluate(
            context.delegation,
            context.tick
        )
