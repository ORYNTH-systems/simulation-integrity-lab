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
from goal_evaluator import GoalEvaluator
from goals import AdmissibleStateGoal, DelegationValidGoal

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
    request_id="goal-001",
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

    node = StateNode(
        node_id=node_id,
        parent_id="root",
        mutation_id=mutation.mutation_id,
        evaluation=evaluation,
        admissible=evaluation["decision"] == "PASS",
        depth=1
    )

    graph.add_node(node)
    graph.add_edge("root", node_id)

evaluator = GoalEvaluator()

admissible_goal = evaluator.evaluate_graph(
    graph,
    AdmissibleStateGoal()
)

delegation_goal = evaluator.evaluate_graph(
    graph,
    DelegationValidGoal()
)

print(json.dumps({
    "admissible_goal": admissible_goal,
    "delegation_goal": delegation_goal,
    "status": "CONSTITUTIONAL_GOAL_EVALUATION_ACTIVE"
}, indent=4))
