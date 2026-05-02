def rob(nums: list[int]) -> int:
    """
    You are a robber planning to rob houses along a street. Adjacent
    houses have security systems — cannot rob two adjacent houses.
    Return the maximum amount you can rob tonight.

    Approach: Bottom-up DP with two rolling variables.
    At each house, decide to rob it (prev2 + current) or skip it (prev1).

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
    >>> rob([1, 2, 3, 1])
    4
    >>> rob([2, 7, 9, 3, 1])
    12
    >>> rob([1])
    1
    >>> rob([2, 1])
    2
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, 0

    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr

    return prev1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")