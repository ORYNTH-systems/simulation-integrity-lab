from mutations.base_mutation import ConstitutionalMutation


class RemoveResources(ConstitutionalMutation):

    mutation_id = "remove_resources"
    description = "Remove requester resources."

    def apply(self, context):
        context.requester.resources["available"] = False


class RestoreResources(ConstitutionalMutation):

    mutation_id = "restore_resources"
    description = "Restore requester resources."

    def apply(self, context):
        context.requester.resources["available"] = True
