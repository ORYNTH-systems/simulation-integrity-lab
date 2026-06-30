class SimulationCluster:

    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def active_nodes(self):
        return [n for n in self.nodes if n.active]
