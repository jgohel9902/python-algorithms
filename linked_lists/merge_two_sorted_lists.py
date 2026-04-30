class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(
    list1: ListNode | None, list2: ListNode | None
) -> ListNode | None:
    """
    Given heads of two sorted linked lists, merge them into one
    sorted linked list and return the head.

    Approach: Iterative using a dummy head node to simplify edge cases.
    Compare nodes one by one and attach the smaller one to result.

    Time Complexity: O(n + m)
    Space Complexity: O(1)

    Examples:
    >>> def make_list(vals):
    ...     dummy = ListNode(0)
    ...     cur = dummy
    ...     for v in vals:
    ...         cur.next = ListNode(v)
    ...         cur = cur.next
    ...     return dummy.next
    >>> def to_list(node):
    ...     result = []
    ...     while node:
    ...         result.append(node.val)
    ...         node = node.next
    ...     return result
    >>> to_list(merge_two_lists(make_list([1,2,4]), make_list([1,3,4])))
    [1, 1, 2, 3, 4, 4]
    >>> to_list(merge_two_lists(make_list([]), make_list([])))
    []
    >>> to_list(merge_two_lists(make_list([]), make_list([0])))
    [0]
    """
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 if list1 else list2

    return dummy.next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")