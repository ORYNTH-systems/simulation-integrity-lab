class StateExplorer:

    def admissible(self, graph):

        return [
            node
            for node in graph.nodes.values()
            if node.admissible
        ]

    def blocked(self, graph):

        return [
            node
            for node in graph.nodes.values()
            if not node.admissible
        ]

    def by_depth(self, graph, depth):

        return [
            node
            for node in graph.nodes.values()
            if node.depth == depth
        ]

    def find_by_mutation(self, graph, mutation_id):

        return [
            node
            for node in graph.nodes.values()
            if node.mutation_id == mutation_id
        ]

    def path_to_root(self, graph, node_id):

        path = []

        current = graph.nodes.get(node_id)

        while current:

            path.append(current.node_id)

            if current.parent_id is None:
                break

            current = graph.nodes.get(current.parent_id)

        return list(reversed(path))
