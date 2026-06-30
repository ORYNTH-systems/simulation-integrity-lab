from copy import deepcopy


class SimulationBranch:

    def fork(self, world):
        return deepcopy(world)
