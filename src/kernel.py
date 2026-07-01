from pipeline import ConstitutionalPipeline

from stages.identity_stage import IdentityStage
from stages.authority_stage import AuthorityStage
from stages.delegation_stage import DelegationStage
from stages.intent_stage import IntentStage


class ConstitutionalKernel:

    def __init__(self):

        self.pipeline = ConstitutionalPipeline()

        self.pipeline.add_stage(IdentityStage())
        self.pipeline.add_stage(AuthorityStage())
        self.pipeline.add_stage(DelegationStage())
        self.pipeline.add_stage(IntentStage())

    def evaluate(self, context):

        return self.pipeline.evaluate(context)
