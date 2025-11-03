# ==============================================================
# Department of Computer Science and Engineering (Cyber Security)
# Subject: AINNCS Practical Exam
# Year: TE
# Date: 03/11/2025
# ==============================================================


# ==============================================================
# Experiment 1: Water Jug Problem using BFS and DFS
# ==============================================================

"""
Theory:
--------
The Water Jug problem is one of the earliest examples of a state-space search problem in AI.
We have two jugs of known capacities (say X liters and Y liters) and need to measure exactly Z liters of water
using only these jugs and the operations: fill, empty, and pour.

The key idea is to represent each possible state as (x, y), where:
- x = amount of water in jug X
- y = amount of water in jug Y

We can then perform operations that move us from one state to another.

Algorithms Used:
1. BFS (Breadth-First Search):
   - Explores all states level-by-level.
   - Guarantees the shortest sequence of actions to reach the goal.
   - Uses a queue for implementation.

2. DFS (Depth-First Search):
   - Explores one path deeply before backtracking.
   - May not find the shortest path but is memory efficient.

Example:
---------
Jug A capacity = 4L
Jug B capacity = 3L
Goal = 2L in any jug

Steps (BFS solution):
(0, 0)
→ (4, 0) Fill Jug A
→ (1, 3) Pour from A to B
→ (1, 0) Empty Jug B
→ (0, 1) Pour from A to B
→ (4, 1) Fill Jug A
→ (2, 3) Pour from A to B  → GOAL REACHED
"""


# ==============================================================
# Experiment 2: 8-Puzzle Problem using A* Algorithm
# ==============================================================

"""
Theory:
--------
The 8-Puzzle problem is a sliding puzzle consisting of eight numbered tiles and one empty space on a 3x3 grid.
The objective is to reach the goal configuration by sliding tiles into the empty space.

A* (A-star) algorithm is a best-first search technique that uses a heuristic to guide the search.
It combines:
    f(n) = g(n) + h(n)
where:
    g(n) = cost to reach node n
    h(n) = heuristic estimate from n to the goal

Common heuristics:
- Misplaced Tile Heuristic (h1): Count of misplaced tiles.
- Manhattan Distance Heuristic (h2): Sum of distances of tiles from their goal positions.

Advantages:
- Guarantees an optimal solution if the heuristic is admissible (never overestimates).

Example:
---------
Initial:
1 2 3
4 _ 6
7 5 8

Goal:
1 2 3
4 5 6
7 8 _

Heuristic (Manhattan distance) guides which move to explore next.
"""


# ==============================================================
# Experiment 3: 8-Puzzle Problem using Hill Climbing Algorithm
# ==============================================================

"""
Theory:
--------
Hill Climbing is a local search algorithm inspired by climbing uphill to reach the peak (goal).
It starts with an initial state and iteratively moves to a neighboring state with a better heuristic value.

Features:
- Greedy algorithm: selects the move that appears best at each step.
- Stops when no neighbor is better (local maximum or plateau).

Drawbacks:
- May get stuck in local maxima or plateaus (requires random restart or simulated annealing to improve).

Example:
---------
Using "number of misplaced tiles" as a heuristic:
Initial → compute h(n)
Move tile → compute new h(n)
If new h(n) < old h(n): accept move
Otherwise: stop (local max)
"""


# ==============================================================
# Experiment 4: Min-Max Algorithm in Game Theory
# ==============================================================

"""
Theory:
--------
Min-Max Algorithm is a backtracking-based decision rule used in two-player games like Tic-Tac-Toe, Chess, etc.
It assumes both players play optimally:
- MAX tries to maximize the score.
- MIN tries to minimize the score.

The algorithm recursively explores all possible moves, applies utility values to terminal states, and backtracks
to decide the best possible move.

Steps:
1. Generate all possible moves.
2. Apply the evaluation function at leaf nodes.
3. Propagate scores upward:
   - MAX chooses the highest value.
   - MIN chooses the lowest value.

Example:
---------
In Tic-Tac-Toe:
- If MAX wins → +10
- If MIN wins → -10
- Draw → 0
The Min-Max algorithm ensures optimal play.
"""


# ==============================================================
# Experiment 5: Alpha-Beta Pruning Algorithm
# ==============================================================

"""
Theory:
--------
Alpha-Beta Pruning improves the efficiency of the Min-Max algorithm.
It skips evaluating branches that cannot influence the final decision (pruning).

Parameters:
- Alpha (α): Best value that MAX can guarantee so far.
- Beta (β): Best value that MIN can guarantee so far.

Pruning Condition:
If α ≥ β at any node, we can stop exploring further down that branch.

Advantages:
- Same result as Min-Max.
- Reduces computation time drastically.

Example:
---------
If a subtree is found to yield worse results than a previously explored one,
it is ignored (pruned), saving processing time.
"""


# ==============================================================
# Experiment 6: Decision Tree
# ==============================================================

"""
Theory:
--------
A Decision Tree is a supervised machine learning model used for classification and regression.
It splits the dataset into subsets based on the value of input features.

Structure:
- Root Node: Represents the entire dataset.
- Internal Nodes: Represent decisions on attributes.
- Branches: Represent outcomes.
- Leaves: Represent class labels or outcomes.

Splitting Criteria:
- Information Gain (ID3 Algorithm)
- Gini Impurity (CART Algorithm)
- Entropy

Advantages:
- Easy to understand and interpret.
- Works well for both categorical and numerical data.

Example:
---------
PlayTennis Dataset:
If Outlook = Sunny AND Humidity = High → No
If Outlook = Sunny AND Humidity = Normal → Yes
If Outlook = Overcast → Yes
If Outlook = Rain AND Wind = Strong → No
If Outlook = Rain AND Wind = Weak → Yes
"""


# ==============================================================
# Experiment 7: Support Vector Machine (SVM)
# ==============================================================

"""
Theory:
--------
Support Vector Machine (SVM) is a powerful supervised learning algorithm used for classification and regression.

Concept:
- SVM finds the optimal hyperplane that best separates data points of different classes.
- The goal is to maximize the margin — the distance between the hyperplane and the nearest data points (support vectors).

For non-linearly separable data, kernel functions are used to project data into higher-dimensional space:
1. Linear Kernel
2. Polynomial Kernel
3. RBF (Radial Basis Function) Kernel

Advantages:
- Effective in high-dimensional spaces.
- Works well even when dimensions > samples.

Example:
---------
Consider two classes of points in 2D space.
SVM draws a line (hyperplane) that separates the classes with maximum margin.
If data is non-linear, RBF kernel maps data to a higher dimension for separation.
"""

# ==============================================================
# END OF AINNCS PRACTICAL EXPERIMENT THEORIES
# ==============================================================