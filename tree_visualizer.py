from copy import deepcopy


class TreeCollector:
    def __init__(self):
        self.nodes = []

    def add(self, player, state_max, state_min, action, value):
        self.nodes.append({
            "player": player,
            "state_max": deepcopy(state_max),
            "state_min": deepcopy(state_min),
            "action": action,
            "value": value
        })

    def print_tree(self):
        for n in self.nodes:
            print(n)