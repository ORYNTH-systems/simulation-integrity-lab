from pipeline import ConstitutionalPipeline

from stages.identity_stage import IdentityStage
from stages.authority_stage import AuthorityStage
from stages.delegation_stage import DelegationStage
from stages.intent_stage import IntentStage
from stages.resource_stage import ResourceStage
from stages.world_stage import WorldStage


class ConstitutionalKernel:

    def __init__(self):

        self.pipeline = ConstitutionalPipeline()

        self.pipeline.add_stage(IdentityStage())
        self.pipeline.add_stage(AuthorityStage())
        self.pipeline.add_stage(DelegationStage())
        self.pipeline.add_stage(IntentStage())
        self.pipeline.add_stage(ResourceStage())
        self.pipeline.add_stage(WorldStage())

    def evaluate(self, context):

        return self.pipeline.evaluate(context)
