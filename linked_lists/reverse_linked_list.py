class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    """
    Given the head of a singly linked list, reverse the list and
    return the reversed list's head.

    Approach: Iterative — track prev, curr, next pointers.

    Time Complexity: O(n)
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
    >>> to_list(reverse_linked_list(make_list([1, 2, 3, 4, 5])))
    [5, 4, 3, 2, 1]
    >>> to_list(reverse_linked_list(make_list([1, 2])))
    [2, 1]
    >>> reverse_linked_list(None) is None
    True
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")