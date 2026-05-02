def climb_stairs(n: int) -> int:
    """
    You are climbing a staircase with n steps. Each time you can
    climb 1 or 2 steps. Return the number of distinct ways to
    reach the top.

    Approach: Bottom-up DP — each step's ways = sum of previous
    two steps (similar to Fibonacci sequence).

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
    >>> climb_stairs(1)
    1
    >>> climb_stairs(2)
    2
    >>> climb_stairs(3)
    3
    >>> climb_stairs(5)
    8
    >>> climb_stairs(10)
    89
    """
    if n <= 2:
        return n

    prev, curr = 1, 2

    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")