def quick_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using Quick Sort — select a pivot, partition the
    array so smaller elements go left and larger go right, then
    recursively sort both partitions.

    Approach: Recursive with last element as pivot (Lomuto scheme).
    Returns a new sorted list without modifying the original.

    Time Complexity:
        Best Case:    O(n log n) — balanced partitions
        Average Case: O(n log n)
        Worst Case:   O(n²)     — already sorted, poor pivot choice
    Space Complexity: O(n log n) — recursion stack
    Stable: No

    Examples:
    >>> quick_sort([10, 7, 8, 9, 1, 5])
    [1, 5, 7, 8, 9, 10]
    >>> quick_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> quick_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> quick_sort([1])
    [1]
    >>> quick_sort([])
    []
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")