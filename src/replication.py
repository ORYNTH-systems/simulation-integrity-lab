class ReplicationEngine:

    def replicate(self, source_node, cluster):
        for node in cluster.active_nodes():
            node.constitutional_hash = source_node.constitutional_hash
