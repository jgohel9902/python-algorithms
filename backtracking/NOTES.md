# Backtracking Notes

## Generate Parentheses
- **Approach:** build the string one character at a time. Add "(" while fewer than n are used. Add ")" only while closed < opened.
- **Time:** O(4^n / sqrt(n)), the nth Catalan number of results, each of length 2n.
- **Space:** O(n) recursion depth, plus the output.
- **Key insight:** never place a ")" that has no matching "(", so every string built is valid and nothing needs to be filtered afterward.