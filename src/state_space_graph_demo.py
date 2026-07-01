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
    request_id="graph-001",
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

    graph.add_edge(
        "root",
        node_id
    )

print(json.dumps({
    "summary": graph.summary(),
    "admissible_nodes": [
        {
            "node_id": node.node_id,
            "mutation_id": node.mutation_id
        }
        for node in graph.admissible_nodes()
    ],
    "blocked_nodes": [
        {
            "node_id": node.node_id,
            "mutation_id": node.mutation_id,
            "reason": node.evaluation["reason"]
        }
        for node in graph.blocked_nodes()
    ],
    "status": "CONSTITUTIONAL_STATE_SPACE_GRAPH_ACTIVE"
}, indent=4))
