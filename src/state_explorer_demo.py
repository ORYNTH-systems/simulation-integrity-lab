import json
import uuid

from world import WorldState
from entity import RichEntity
from delegation import Delegation
from execution_request import ExecutionRequest
from execution_context import ExecutionContext

from kernel import ConstitutionalKernel
from mutation_library import MutationLibrary
from counterfactual import CounterfactualEngine
from state_node import StateNode
from state_space_graph import StateSpaceGraph
from state_explorer import StateExplorer

world = WorldState()

entity = RichEntity(
    entity_id="robot",
    entity_type="robot"
)

delegation = Delegation(
    delegation_id="del",
    delegator_id="controller",
    delegatee_id="robot",
    authority_scope="execute",
    expires_at_tick=10
)

request = ExecutionRequest(
    request_id="explore-001",
    requester="robot",
    action="move",
    target="zoneA",
    payload={}
)

context = ExecutionContext(
    world,
    entity,
    delegation,
    request,
    tick=5
)

kernel = ConstitutionalKernel()
counterfactual = CounterfactualEngine()
graph = StateSpaceGraph()
explorer = StateExplorer()

root_eval = kernel.evaluate(context)

root = StateNode(
    node_id="root",
    parent_id=None,
    mutation_id="baseline",
    evaluation=root_eval,
    admissible=root_eval["decision"] == "PASS",
    depth=0
)

graph.add_node(root)

last_node_id = "root"

for mutation in MutationLibrary().mutations:

    evaluation = counterfactual.evaluate(
        kernel,
        context,
        mutation.apply
    )

    node_id = str(uuid.uuid4())

    child = StateNode(
        node_id=node_id,
        parent_id="root",
        mutation_id=mutation.mutation_id,
        evaluation=evaluation,
        admissible=evaluation["decision"] == "PASS",
        depth=1
    )

    graph.add_node(child)
    graph.add_edge("root", node_id)

    last_node_id = node_id

output = {
    "summary": graph.summary(),
    "admissible_count": len(explorer.admissible(graph)),
    "blocked_count": len(explorer.blocked(graph)),
    "depth_1_count": len(explorer.by_depth(graph, 1)),
    "expire_delegation_nodes": [
        node.node_id
        for node in explorer.find_by_mutation(
            graph,
            "expire_delegation"
        )
    ],
    "path_to_last_node": explorer.path_to_root(
        graph,
        last_node_id
    ),
    "status": "CONSTITUTIONAL_STATE_EXPLORATION_ACTIVE"
}

print(json.dumps(output, indent=4))
