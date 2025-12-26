MAX_STATE = [1, 1, 6, 2, 2, 1]

DEPENDENCIES = {
    0: [],      # Corpo
    1: [0],     # Cabeça
    2: [0],     # Perna
    3: [1],     # Olho
    4: [1],     # Antena
    5: [0]      # Rabo
}

def is_terminal(state):
    return state == MAX_STATE

def can_add(state, part):
    if state[part] >= MAX_STATE[part]:
        return False
    for dep in DEPENDENCIES[part]:
        if state[dep] == 0:
            return False
    return True

def apply_roll(state, roll):
    part = roll - 1
    if can_add(state, part):
        new_state = state.copy()
        new_state[part] += 1
        return new_state
    return state