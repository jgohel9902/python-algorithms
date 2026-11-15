"""Min Stack: a stack that returns its minimum element in O(1)."""


class MinStack:
    """
    >>> s = MinStack()
    >>> s.push(5)
    >>> s.push(2)
    >>> s.push(7)
    >>> s.get_min()
    2
    >>> s.pop()
    7
    >>> s.top()
    2
    >>> s.pop()
    2
    >>> s.get_min()
    5
    >>> s.pop()
    5
    >>> s.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty stack
    """

    def __init__(self) -> None:
        # Each entry is (value, minimum of the stack up to this entry)
        self._stack: list[tuple[int, int]] = []

    def push(self, value: int) -> None:
        current_min = min(value, self._stack[-1][1]) if self._stack else value
        self._stack.append((value, current_min))

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("pop from empty stack")
        return self._stack.pop()[0]

    def top(self) -> int:
        if not self._stack:
            raise IndexError("top from empty stack")
        return self._stack[-1][0]

    def get_min(self) -> int:
        if not self._stack:
            raise IndexError("get_min from empty stack")
        return self._stack[-1][1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()