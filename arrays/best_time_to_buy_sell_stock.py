def max_profit(prices: list[int]) -> int:
    """
    Given an array of stock prices, return the maximum profit by buying
    on one day and selling on a later day. Return 0 if no profit possible.

    Approach: Single pass — track minimum price seen so far and
    calculate profit at each step.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    >>> max_profit([7, 6, 4, 3, 1])
    0
    >>> max_profit([2, 4, 1])
    2
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")