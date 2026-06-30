class ExecutionGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def connect(self, parent, child):
        self.edges.append((parent, child))
