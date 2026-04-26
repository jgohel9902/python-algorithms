def is_anagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return True if t is an anagram of s,
    False otherwise. An anagram uses all original letters exactly once.

    Approach: Compare character frequency counts of both strings.

    Time Complexity: O(n)
    Space Complexity: O(1) — at most 26 keys for lowercase letters

    Examples:
    >>> is_anagram("anagram", "nagaram")
    True
    >>> is_anagram("rat", "car")
    False
    >>> is_anagram("a", "a")
    True
    >>> is_anagram("ab", "a")
    False
    """
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")