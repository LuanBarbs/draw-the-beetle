from copy import deepcopy

FINAL_STATE = [1, 1, 6, 2, 2, 1]

class BeetleGame:

    def initial_state(self):
        return [0, 0, 0, 0, 0, 0]

    def is_terminal(self, state):
        return state == FINAL_STATE

    def valid_actions(self, state):
        actions = []

        # Corpo
        if state[0] < 1:
            actions.append(0)

        # Cabeça
        if state[0] == 1 and state[1] < 1:
            actions.append(1)

        # Pernas
        if state[0] == 1 and state[2] < 6:
            actions.append(2)

        # Olhos
        if state[1] == 1 and state[3] < 2:
            actions.append(3)

        # Antenas
        if state[1] == 1 and state[4] < 2:
            actions.append(4)

        # Rabo
        if state[0] == 1 and state[5] < 1:
            actions.append(5)

        return actions

    def apply_action(self, state, action):
        # validate action against current state rules
        if action not in self.valid_actions(state):
            raise ValueError(f"Invalid action {action} for state {state}")
        new_state = deepcopy(state)
        new_state[action] += 1
        return new_state