def product_except_self(nums: list[int]) -> list[int]:
    """
    Given an integer array, return an array where each element is
    the product of all elements except itself.
    Must solve without division in O(n) time.

    Approach: Two passes — prefix products left to right, then
    suffix products right to left. Multiply both at each index.

    Time Complexity: O(n)
    Space Complexity: O(1) excluding output array

    Examples:
    >>> product_except_self([1, 2, 3, 4])
    [24, 12, 8, 6]
    >>> product_except_self([-1, 1, 0, -3, 3])
    [0, 0, 9, 0, 0]
    >>> product_except_self([1, 1])
    [1, 1]
    """
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")