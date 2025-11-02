import heapq

# Goal state for reference
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Possible moves: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_blank(state):
    """Finds the position of the blank (0) tile."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def manhattan_distance(state):
    """Heuristic: sum of Manhattan distances of tiles from their goal positions."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance


def is_goal(state):
    return state == goal_state


def get_neighbors(state):
    """Generate all possible next states."""
    x, y = find_blank(state)
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors


def state_to_tuple(state):
    """Convert 2D list to tuple for hashing."""
    return tuple(tuple(row) for row in state)


def a_star(start_state):
    """A* Search Algorithm"""
    pq = []
    g_cost = {state_to_tuple(start_state): 0}
    heapq.heappush(pq, (manhattan_distance(start_state), 0, start_state, []))

    visited = set()

    while pq:
        f, cost, current, path = heapq.heappop(pq)
        if state_to_tuple(current) in visited:
            continue

        visited.add(state_to_tuple(current))

        if is_goal(current):
            return path + [current]

        for neighbor in get_neighbors(current):
            n_tuple = state_to_tuple(neighbor)
            new_cost = cost + 1
            if n_tuple not in g_cost or new_cost < g_cost[n_tuple]:
                g_cost[n_tuple] = new_cost
                f_score = new_cost + manhattan_distance(neighbor)
                heapq.heappush(pq, (f_score, new_cost, neighbor, path + [current]))

    return None


def print_state(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()


# Example start state
start_state = [
    [1, 2, 3],
    [5, 0, 6],
    [4, 7, 8]
]

print("Initial State:")
print_state(start_state)

solution = a_star(start_state)

if solution:
    print(f"Solution found in {len(solution) - 1} moves!\n")
    for i, step in enumerate(solution):
        print(f"Step {i}:")
        print_state(step)
else:
    print("No solution found.")
