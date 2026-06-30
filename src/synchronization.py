class SynchronizationEngine:

    def synchronize(self, cluster):
        hashes = {
            node.constitutional_hash
            for node in cluster.active_nodes()
        }

        return {
            "synchronized": len(hashes) == 1,
            "constitutional_hashes": list(hashes)
        }
