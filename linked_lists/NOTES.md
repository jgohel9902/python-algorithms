# Linked Lists

## Reverse Linked List
- **Approach:** Iterative with prev, curr, next pointers
- **Time:** O(n) — single pass
- **Space:** O(1) — only pointer variables
- **Key insight:** At each step, reverse the current node's pointer
  to point backward, then advance all three pointers forward