def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using Bubble Sort — repeatedly compare adjacent
    elements and swap if in wrong order. Early exit if no swaps
    occur in a full pass (already sorted).

    Approach: Nested loops with swapped flag optimization.

    Time Complexity:
        Best Case:    O(n)   — already sorted, early exit
        Average Case: O(n²)
        Worst Case:   O(n²)  — reverse sorted
    Space Complexity: O(1) — in-place sorting
    Stable: Yes

    Examples:
    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> bubble_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([1])
    [1]
    >>> bubble_sort([])
    []
    """
    n = len(arr)
    arr = arr.copy()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")