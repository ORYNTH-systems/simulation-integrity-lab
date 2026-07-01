from kernel import ConstitutionalKernel


class ConstitutionalExecutionEngine:

    def __init__(self):

        self.kernel = ConstitutionalKernel()

    def evaluate(self, context):

        return self.kernel.evaluate(context)
