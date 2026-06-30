from copy import deepcopy


class SimulationBranchManager:

    def create_branch(self, world, branch_name):
        return {
            "name": branch_name,
            "world": deepcopy(world)
        }

    def list_branches(self, branches):
        return [b["name"] for b in branches]

    def compare(self, branch_a, branch_b):
        return {
            "same_tick": branch_a["world"].tick == branch_b["world"].tick,
            "same_safety": branch_a["world"].safety == branch_b["world"].safety,
            "same_constraints": branch_a["world"].constraints == branch_b["world"].constraints,
            "same_artifact": branch_a["world"].artifact == branch_b["world"].artifact
        }
