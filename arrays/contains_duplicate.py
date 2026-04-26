def contains_duplicate(nums: list[int]) -> bool:
    """
    Given an integer array, return True if any value appears at least twice,
    False if all elements are distinct.

    Approach: Hash set — add each number, if already in set return True.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Examples:
    >>> contains_duplicate([1, 2, 3, 1])
    True
    >>> contains_duplicate([1, 2, 3, 4])
    False
    >>> contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    True
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")