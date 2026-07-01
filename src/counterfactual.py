from copy import deepcopy


class CounterfactualEngine:

    def evaluate(

        self,

        kernel,

        context,

        mutator

    ):

        new_context = deepcopy(context)

        mutator(new_context)

        return kernel.evaluate(new_context)
