import random
import copy

# Define goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Possible moves: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def manhattan_distance(state):
    """Heuristic: total Manhattan distance of all tiles from goal positions."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance


def get_neighbors(state):
    """Generate all possible next states from the current state."""
    x, y = find_blank(state)
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors


def print_state(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()


def hill_climb(start_state, max_iterations=1000):
    """Hill Climbing algorithm for 8-puzzle."""
    current_state = start_state
    current_heuristic = manhattan_distance(current_state)
    steps = 0

    print("Initial State:")
    print_state(current_state)

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_state)
        neighbor_heuristics = [(manhattan_distance(n), n) for n in neighbors]

        # Select the neighbor with the lowest heuristic
        best_heuristic, best_neighbor = min(neighbor_heuristics, key=lambda x: x[0])

        if best_heuristic >= current_heuristic:
            # No improvement — local maxima
            print("Reached a local optimum!")
            break

        # Move to better state
        current_state = best_neighbor
        current_heuristic = best_heuristic
        steps += 1

        print(f"Step {steps}: (Heuristic = {current_heuristic})")
        print_state(current_state)

        if current_heuristic == 0:
            print("Goal state reached successfully!")
            return

    if current_heuristic != 0:
        print("Failed to reach goal — trapped in local optimum.")


# Example start state
start_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

hill_climb(start_state)


# start_state = [
#     [1, 3, 4],
#     [8, 6, 2],
#     [7, 0, 5]
# ]


# start_state = [
#     [2, 8, 3],
#     [1, 6, 4],
#     [7, 0, 5]
# ]
