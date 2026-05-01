# Dynamic Programming

## Climbing Stairs
- **Approach:** Bottom-up DP, rolling two variables (no array needed)
- **Time:** O(n) — single pass
- **Space:** O(1) — only two variables instead of full DP array
- **Key insight:** Ways to reach step n = ways to reach step n-1
  plus ways to reach step n-2 — identical to Fibonacci sequence
- **Base cases:** n=1 → 1 way, n=2 → 2 ways