from mutations.base_mutation import ConstitutionalMutation


class RevokeAuthority(ConstitutionalMutation):

    mutation_id = "revoke_authority"
    description = "Deactivate requester authority."

    def apply(self, context):
        context.requester.authority["active"] = False


class GrantAuthority(ConstitutionalMutation):

    mutation_id = "grant_authority"
    description = "Activate requester authority."

    def apply(self, context):
        context.requester.authority["active"] = True
