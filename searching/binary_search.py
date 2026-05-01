def binary_search(nums: list[int], target: int) -> int:
    """
    Given a sorted array and a target value, return the index of the
    target using binary search. Return -1 if target is not found.

    Approach: Iterative — maintain left and right pointers, check
    the middle element each iteration and narrow the search range.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Examples:
    >>> binary_search([-1, 0, 3, 5, 9, 12], 9)
    4
    >>> binary_search([-1, 0, 3, 5, 9, 12], 2)
    -1
    >>> binary_search([5], 5)
    0
    >>> binary_search([], 5)
    -1
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")