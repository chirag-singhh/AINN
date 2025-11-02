import math

def minimax(depth, node_index, is_maximizing_player, values, max_depth, alpha, beta):
    # Base case: reached leaf node
    if depth == max_depth:
        return values[node_index]

    if is_maximizing_player:
        best = -math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, max_depth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # alpha-beta pruning
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, max_depth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


# Example: 4 leaf values = depth of 2 (since 2^2 = 4)
values = [3, 5, 6, 9, 1, 2, 0, -1]


# Calculate tree depth automatically
max_depth = math.log2(len(values))
if not max_depth.is_integer():
    raise ValueError("Number of leaf nodes must be a power of 2.")

max_depth = int(max_depth)

print("Leaf node values:", values)
optimal_value = minimax(0, 0, True, values, max_depth, -math.inf, math.inf)
print("\nOptimal value:", optimal_value)
