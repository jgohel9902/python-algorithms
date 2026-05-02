# Sorting

## Bubble Sort
- **Approach:** Nested loops, swap adjacent elements if out of order
- **Time Best:** O(n) — swapped flag exits early if already sorted
- **Time Avg/Worst:** O(n²) — nested iterations
- **Space:** O(1) — in-place, returns a copy here for safety
- **Stable:** Yes — equal elements never swapped
- **Key insight:** After each outer pass, the largest unsorted element
  bubbles to its correct position at the end