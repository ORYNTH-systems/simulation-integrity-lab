class ReplayVerifier:

    def verify(self, history_a, history_b):

        if len(history_a) != len(history_b):
            return False

        for left, right in zip(history_a, history_b):

            if left != right:
                return False

        return True
