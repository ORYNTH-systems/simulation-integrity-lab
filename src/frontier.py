class Frontier:

    def __init__(self):
        self.nodes = []

    def push(self, node):
        self.nodes.append(node)

    def pop(self):
        self.nodes.sort(key=lambda n: n.score, reverse=True)
        return self.nodes.pop(0)

    def empty(self):
        return len(self.nodes) == 0
