def max_subarray(nums: list[int]) -> int:
    """
    Given an integer array, find the subarray with the largest
    sum and return its sum. Known as Kadane's Algorithm.

    Approach: Single pass — track current running sum and global
    maximum. Reset current sum if it drops below zero.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
    >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> max_subarray([1])
    1
    >>> max_subarray([5, 4, -1, 7, 8])
    23
    >>> max_subarray([-1, -2, -3])
    -1
    """
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")