# Linked Lists

## Reverse Linked List
- **Approach:** Iterative with prev, curr, next pointers
- **Time:** O(n) — single pass
- **Space:** O(1) — only pointer variables
- **Key insight:** At each step, reverse the current node's pointer
  to point backward, then advance all three pointers forward

  ## Merge Two Sorted Lists
- **Approach:** Dummy head node + iterative comparison
- **Time:** O(n + m) — traverse both lists once
- **Space:** O(1) — only pointer manipulation, no extra list
- **Key insight:** Dummy head removes edge case of empty result list,
  attach remaining non-null list at the end directly

  ## Linked List Cycle Detection
- **Approach:** Floyd's Cycle Detection (tortoise and hare)
- **Time:** O(n) — fast pointer laps slow pointer within n steps
- **Space:** O(1) — only two pointer variables
- **Key insight:** If a cycle exists, fast pointer will eventually
  lap slow pointer and they will meet inside the cycle.
  If no cycle, fast pointer reaches None first.
- **Classic alternative:** Hash set to track visited nodes — O(n)
  time but O(n) space, Floyd's is superior