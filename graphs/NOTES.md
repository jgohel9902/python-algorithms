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

  ## Flood Fill
- **Approach:** DFS from starting pixel, fill all connected pixels
  matching the original color
- **Time:** O(m * n) — each pixel visited at most once
- **Space:** O(m * n) — recursion stack worst case
- **Key insight:** Early exit if new color equals original color —
  prevents infinite recursion
- **Difference from Number of Islands:** Fills with a new value
  instead of marking visited, works on integers not strings

  ## Word Search
- **Approach:** Backtracking DFS from every cell as starting point
- **Time:** O(m * n * 4^L) — L = word length, 4 directions each step
- **Space:** O(L) — recursion stack depth = word length
- **Key insight:** Mark visited cells with "#" temporarily to prevent
  reuse in same path. Restore original value after backtracking.
- **Early exit:** Return True as soon as word is found — no need
  to explore remaining cells
- **vs Flood Fill/Islands:** Uses backtracking to restore state,
  not permanent marking