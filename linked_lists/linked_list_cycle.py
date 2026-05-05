class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """
    Given the head of a linked list, return True if the list has
    a cycle, False otherwise.

    Approach: Floyd's Cycle Detection — slow pointer moves 1 step,
    fast pointer moves 2 steps. If they meet, cycle exists.
    If fast reaches None, no cycle.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
    >>> def make_cycle(vals, pos):
    ...     nodes = [ListNode(v) for v in vals]
    ...     for i in range(len(nodes) - 1):
    ...         nodes[i].next = nodes[i + 1]
    ...     if pos != -1:
    ...         nodes[-1].next = nodes[pos]
    ...     return nodes[0] if nodes else None
    >>> has_cycle(make_cycle([3, 2, 0, -4], 1))
    True
    >>> has_cycle(make_cycle([1, 2], 0))
    True
    >>> has_cycle(make_cycle([1], -1))
    False
    >>> has_cycle(None)
    False
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")