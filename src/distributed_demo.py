import json

from node import SimulationNode
from cluster import SimulationCluster
from synchronization import SynchronizationEngine
from replication import ReplicationEngine
from consistency import ConsistencyEngine


def main():
    cluster = SimulationCluster()

    node_a = SimulationNode(
        node_id="node_a",
        constitutional_hash="HASH-A"
    )

    node_b = SimulationNode(
        node_id="node_b",
        constitutional_hash="HASH-B"
    )

    cluster.add_node(node_a)
    cluster.add_node(node_b)

    sync_before = SynchronizationEngine().synchronize(cluster)
    consistency_before = ConsistencyEngine().evaluate(sync_before)

    ReplicationEngine().replicate(node_a, cluster)

    sync_after = SynchronizationEngine().synchronize(cluster)
    consistency_after = ConsistencyEngine().evaluate(sync_after)

    output = {
        "before_replication": {
            "sync": sync_before,
            "consistency": consistency_before
        },
        "after_replication": {
            "sync": sync_after,
            "consistency": consistency_after
        },
        "status": "DISTRIBUTED_CONSTITUTIONAL_EXECUTION_ACTIVE"
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
