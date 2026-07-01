class StateSpaceGraph:

    def __init__(self):

        self.nodes = {}

        self.edges = []

    def add_node(self, node):

        self.nodes[node.node_id] = node

    def add_edge(self, parent_id, child_id):

        self.edges.append({
            "parent": parent_id,
            "child": child_id
        })

    def admissible_nodes(self):

        return [
            node
            for node in self.nodes.values()
            if node.admissible
        ]

    def blocked_nodes(self):

        return [
            node
            for node in self.nodes.values()
            if not node.admissible
        ]

    def summary(self):

        return {
            "nodes": len(self.nodes),
            "edges": len(self.edges),
            "admissible": len(self.admissible_nodes()),
            "blocked": len(self.blocked_nodes())
        }
