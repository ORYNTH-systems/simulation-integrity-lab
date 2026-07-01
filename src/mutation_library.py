from mutations.delegation_mutations import ExpireDelegation, RenewDelegation
from mutations.authority_mutations import RevokeAuthority, GrantAuthority
from mutations.resource_mutations import RemoveResources, RestoreResources


class MutationLibrary:

    def __init__(self):
        self.mutations = [
            ExpireDelegation(),
            RenewDelegation(),
            RevokeAuthority(),
            GrantAuthority(),
            RemoveResources(),
            RestoreResources()
        ]

    def candidates(self):
        return [
            mutation.candidate()
            for mutation in self.mutations
        ]
