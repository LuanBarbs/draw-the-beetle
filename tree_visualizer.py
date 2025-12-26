from beetle_game import apply_roll

def print_tree(state, depth, max_depth, prefix="", use_ab=False):
    if depth == max_depth:
        print(prefix + f"Estado: {state}")
        return

    for roll in range(1, 7):
        next_state = apply_roll(state, roll)
        print(prefix + f"Dado: {roll} -> {next_state}")
        print_tree(
            next_state,
            depth + 1,
            max_depth,
            prefix + "  ",
            use_ab
        )