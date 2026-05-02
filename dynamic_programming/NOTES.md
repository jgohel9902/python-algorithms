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


  ## House Robber
- **Approach:** Two rolling variables instead of full DP array
- **Time:** O(n) — single pass
- **Space:** O(1) — only prev1 and prev2 variables
- **Key insight:** At each house, max = max(skip current = prev1,
  rob current = prev2 + num). Roll variables forward each step.
- **Edge cases:** Empty array returns 0, single house returns nums[0]


## Longest Common Subsequence
- **Approach:** Bottom-up 2D DP table of size (m+1) x (n+1)
- **Time:** O(m * n) — fill entire table
- **Space:** O(m * n) — full DP table stored
- **Key insight:** If chars match → dp[i][j] = dp[i-1][j-1] + 1
  If no match → dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- **Optimization:** Can reduce to O(n) space using two rolling rows