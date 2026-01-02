from copy import deepcopy

FINAL_STATE = [1, 1, 6, 2, 2, 1]

class BeetleGame:
    def initial_state(self):
        return [0, 0, 0, 0, 0, 0]

    def is_terminal(self, state):
        return state == FINAL_STATE

    def valid_actions(self, state):
        actions = []
        if state[0] < 1:
            actions.append(0)
        if state[0] == 1 and state[1] < 1:
            actions.append(1)
        if state[0] == 1 and state[2] < 6:
            actions.append(2)
        if state[1] == 1 and state[3] < 2:
            actions.append(3)
        if state[1] == 1 and state[4] < 2:
            actions.append(4)
        if state[0] == 1 and state[5] < 1:
            actions.append(5)
        return actions

    def apply_action(self, state, action):
        new_state = deepcopy(state)
        if action in self.valid_actions(state):
            new_state[action] += 1
        return new_state