# Trees Notes

## Invert Binary Tree
- **Approach:** swap each node's children. Recursively, or iteratively with a BFS queue.
- **Time:** O(n), every node is visited once.
- **Space:** O(h) recursion depth (O(n) worst case for a skewed tree); the iterative version uses O(w) for the queue, where w is the widest level.
- **Key insight:** inverting is just "swap children at every node", so the order you visit nodes in doesn't matter.