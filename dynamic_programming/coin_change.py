def coin_change(coins: list[int], amount: int) -> int:
    """
    Given coin denominations and a total amount, return the fewest
    number of coins needed to make up that amount.
    Return -1 if amount cannot be made up by any combination.

    Approach: Bottom-up DP — build solution from amount 0 up to
    target. For each amount, try every coin denomination.

    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)

    Examples:
    >>> coin_change([1, 5, 10, 25], 36)
    3
    >>> coin_change([1, 2, 5], 11)
    3
    >>> coin_change([2], 3)
    -1
    >>> coin_change([1], 0)
    0
    >>> coin_change([1], 1)
    1
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")