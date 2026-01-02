# Heurística de Progressão Estrutural

WEIGHTS = [5, 4, 1, 2, 2, 3]
MAX_COUNTS = [1, 1, 6, 2, 2, 1]

def heuristic(state):
    # Normalização por parte máxima
    score = 0.0
    for i in range(6):
        score += WEIGHTS[i] * (state[i] / MAX_COUNTS[i])
    return score