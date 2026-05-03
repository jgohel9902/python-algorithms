# Graphs

## Number of Islands
- **Approach:** DFS from each unvisited land cell, mark visited
  cells as '0' to avoid revisiting
- **Time:** O(m * n) — each cell visited at most once
- **Space:** O(m * n) — recursion stack depth in worst case
  (entire grid is one island)
- **Key insight:** Each DFS call floods an entire island — count
  how many times we trigger DFS = number of islands
- **Note:** Modifies the input grid in place. Pass a deep copy
  if original grid must be preserved.