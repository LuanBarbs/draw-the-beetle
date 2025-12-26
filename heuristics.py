FINAL_STATE = [1, 1, 6, 2, 2, 1]

def heuristic(state_max, state_min):
    def progress(state):
        return sum(state[i] / FINAL_STATE[i] for i in range(6))

    return progress(state_max) - progress(state_min)
