# Strings

## Valid Anagram
- **Approach:** Character frequency map — increment for s, decrement for t
- **Time:** O(n) — two passes
- **Space:** O(1) — max 26 keys (lowercase letters only)
- **Key insight:** If any count goes negative, t has a char s doesn't