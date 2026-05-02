# Sorting

## Bubble Sort
- **Approach:** Nested loops, swap adjacent elements if out of order
- **Time Best:** O(n) — swapped flag exits early if already sorted
- **Time Avg/Worst:** O(n²) — nested iterations
- **Space:** O(1) — in-place, returns a copy here for safety
- **Stable:** Yes — equal elements never swapped
- **Key insight:** After each outer pass, the largest unsorted element
  bubbles to its correct position at the end

  ## Merge Sort
- **Approach:** Divide and conquer — split into halves recursively,
  merge sorted halves back together
- **Time:** O(n log n) — all cases, guaranteed
- **Space:** O(n) — temporary arrays during merge step
- **Stable:** Yes — equal elements maintain original order
- **Key insight:** Split until base case (1 element), then merge
  pairs in sorted order back up the call stack
- **Advantage over Bubble Sort:** Guaranteed O(n log n) vs O(n²)