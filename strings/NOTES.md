# Strings

## Valid Anagram
- **Approach:** Character frequency map — increment for s, decrement for t
- **Time:** O(n) — two passes
- **Space:** O(1) — max 26 keys (lowercase letters only)
- **Key insight:** If any count goes negative, t has a char s doesn't

## Valid Palindrome
- **Approach:** Two pointers moving inward, skipping non-alphanumeric chars
- **Time:** O(n) — single pass
- **Space:** O(1) — no extra data structures
- **Key insight:** Only compare alphanumeric characters, case-insensitive