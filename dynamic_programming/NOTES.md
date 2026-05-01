# Dynamic Programming

## Climbing Stairs
- **Approach:** Bottom-up DP, rolling two variables (no array needed)
- **Time:** O(n) — single pass
- **Space:** O(1) — only two variables instead of full DP array
- **Key insight:** Ways to reach step n = ways to reach step n-1
  plus ways to reach step n-2 — identical to Fibonacci sequence
- **Base cases:** n=1 → 1 way, n=2 → 2 ways


## Maximum Subarray (Kadane's Algorithm)
- **Approach:** Single pass tracking current and global max sum
- **Time:** O(n) — one iteration through array
- **Space:** O(1) — only two variables
- **Key insight:** At each element, decide whether to extend the
  current subarray or start fresh from this element using:
  current_sum = max(num, current_sum + num)
- **Edge case:** Works with all-negative arrays — returns least
  negative number