def two_nums(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers and a target, return indices of the two numbers that add up to the target.
    
    Approahc: Hash map  - store seen values and check complement each step.
    
    Time Complexity: 0(n)
    Space Complexity: 0(n)
    
    Examples:
    >>> two_sum([2,7,11,15], 9)
    [0, 1]
    
    >>> two_sum([3,2,4], 6)
    [1, 2]
    
    >>> two_sum([3,3], 6)
    [0, 1]
    """
    
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
        return []
    
    if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed!")