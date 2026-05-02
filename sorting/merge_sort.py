def merge_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using Merge Sort — recursively divide the array
    into halves, sort each half, then merge back in sorted order.

    Approach: Divide and conquer — split until single elements,
    then merge pairs in sorted order back up the call stack.

    Time Complexity:
        Best Case:    O(n log n)
        Average Case: O(n log n)
        Worst Case:   O(n log n)
    Space Complexity: O(n) — temporary arrays during merge
    Stable: Yes

    Examples:
    >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
    >>> merge_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> merge_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> merge_sort([1])
    [1]
    >>> merge_sort([])
    []
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists into one sorted list.

    >>> _merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> _merge([], [1, 2])
    [1, 2]
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")