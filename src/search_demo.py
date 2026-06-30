import json
from copy import deepcopy

from simulation import Simulation
from search import SearchNode
from frontier import Frontier
from heuristic import ConstitutionalHeuristic
from pruning import ConstitutionalPruner
from execution_graph import ExecutionGraph

sim = Simulation()
sim.run(5)

frontier = Frontier()
graph = ExecutionGraph()
heuristic = ConstitutionalHeuristic()
pruner = ConstitutionalPruner()

root = SearchNode(
    node_id="root",
    world=deepcopy(sim.world),
    depth=0
)

root.score = heuristic.score(root.world)

frontier.push(root)
graph.add_node(root)

expanded = []

while not frontier.empty():

    node = frontier.pop()

    if not pruner.admissible(node.world):
        continue

    expanded.append({
        "node": node.node_id,
        "score": node.score
    })

print(json.dumps({
    "expanded": expanded,
    "graph_nodes": len(graph.nodes),
    "graph_edges": len(graph.edges),
    "status":"CONSTITUTIONAL_SEARCH_ACTIVE"
}, indent=2))
