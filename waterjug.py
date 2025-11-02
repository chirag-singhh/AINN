from collections import deque

def bfs_water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))  # initial state (jug1, jug2)
    path = []

    while queue:
        a, b = queue.popleft()

        # Skip already visited states
        if (a, b) in visited:
            continue

        visited.add((a, b))
        path.append((a, b))

        # Goal check
        if a == target or b == target:
            print("Goal reached using BFS!")
            for step in path:
                print(step)
            return

        # Generate all possible next states
        possible_states = [
            (jug1, b),          # fill jug1
            (a, jug2),          # fill jug2
            (0, b),             # empty jug1
            (a, 0),             # empty jug2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),  # pour jug1 -> jug2
            (a + min(b, jug1 - a), b - min(b, jug1 - a))   # pour jug2 -> jug1
        ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)

    print("No solution found using BFS.")
    
def dfs_water_jug(jug1, jug2, target):
    visited = set()

    def dfs(a, b, path):
        # If already visited, skip
        if (a, b) in visited:
            return False

        visited.add((a, b))
        path.append((a, b))

        # Goal check
        if a == target or b == target:
            print("Goal reached using DFS!")
            for step in path:
                print(step)
            return True

        # Generate possible next states
        possible_states = [
            (jug1, b),          # fill jug1
            (a, jug2),          # fill jug2
            (0, b),             # empty jug1
            (a, 0),             # empty jug2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),  # pour jug1 -> jug2
            (a + min(b, jug1 - a), b - min(b, jug1 - a))   # pour jug2 -> jug1
        ]

        for state in possible_states:
            if dfs(state[0], state[1], path.copy()):
                return True
        return False

    if not dfs(0, 0, []):
        print("No solution found using DFS.")



# Example: 4-liter and 3-liter jugs, target = 2 liters
jug1 = 4
jug2 = 3
target = 2

print("\n--- BFS Solution ---")
bfs_water_jug(jug1, jug2, target)

print("\n--- DFS Solution ---")
dfs_water_jug(jug1, jug2, target)
