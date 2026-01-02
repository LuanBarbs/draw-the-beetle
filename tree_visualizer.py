class TreeCollector:
    def __init__(self):
        self.nodes = []

    def add(self, node_type, state_max, state_min, action, value):
        self.nodes.append(
            (node_type, tuple(state_max), tuple(state_min), action, value)
        )

    def print_tree(self):
        for node in self.nodes:
            print(node)