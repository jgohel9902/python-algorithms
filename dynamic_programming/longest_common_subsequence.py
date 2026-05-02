def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Given two strings, return the length of their longest common
    subsequence. A subsequence appears in the same relative order
    but not necessarily contiguous.

    Approach: Bottom-up 2D DP table. If characters match, extend
    the previous diagonal. Otherwise take the max of left or above.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    Examples:
    >>> longest_common_subsequence("abcde", "ace")
    3
    >>> longest_common_subsequence("abc", "abc")
    3
    >>> longest_common_subsequence("abc", "def")
    0
    >>> longest_common_subsequence("bl", "yby")
    1
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")