from mutations.base_mutation import ConstitutionalMutation


class ExpireDelegation(ConstitutionalMutation):

    mutation_id = "expire_delegation"
    description = "Force delegation to expire before execution."

    def apply(self, context):
        context.delegation.expires_at_tick = 0


class RenewDelegation(ConstitutionalMutation):

    mutation_id = "renew_delegation"
    description = "Extend delegation beyond current execution tick."

    def apply(self, context):
        context.delegation.expires_at_tick = context.tick + 10
        context.delegation.active = True
