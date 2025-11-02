import math

def alphabeta(depth, node_index, is_maximizing_player, values, max_depth, alpha, beta):
    """
    Alpha-Beta Pruning implementation.
    - depth: current depth in the game tree
    - node_index: index of current node in the tree
    - is_maximizing_player: True if it's MAX's turn, False if MIN's
    - values: list of terminal (leaf) node values
    - max_depth: maximum tree depth
    - alpha: best value Maximizer can guarantee
    - beta: best value Minimizer can guarantee
    """
    # Base case (leaf node)
    if depth == max_depth:
        return values[node_index]

    if is_maximizing_player:
        best = -math.inf
        for i in range(2):  # two children per node
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, max_depth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Prune the remaining branches
            if beta <= alpha:
                print(f"Pruned at depth {depth}, node {node_index} (α={alpha}, β={beta})")
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, max_depth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruned at depth {depth}, node {node_index} (α={alpha}, β={beta})")
                break
        return best


# Example leaf node values (8 nodes → tree of depth 3)
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Compute tree depth automatically
max_depth = int(math.log2(len(values)))

print("Leaf values:", values)

optimal_value = alphabeta(0, 0, True, values, max_depth, -math.inf, math.inf)

print("\nOptimal value (with Alpha-Beta Pruning):", optimal_value)
