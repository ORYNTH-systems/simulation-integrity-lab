from pipeline import ConstitutionalPipeline

from stages.identity_stage import IdentityStage
from stages.delegation_stage import DelegationStage


class ConstitutionalKernel:

    def __init__(self):

        self.pipeline = ConstitutionalPipeline()

        self.pipeline.add_stage(
            IdentityStage()
        )

        self.pipeline.add_stage(
            DelegationStage()
        )

    def evaluate(self, context):

        return self.pipeline.evaluate(context)
