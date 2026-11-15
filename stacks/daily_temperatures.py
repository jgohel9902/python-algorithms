"""Daily Temperatures: days to wait for a warmer temperature, O(n) with a monotonic stack."""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    >>> daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
    [1, 1, 4, 2, 1, 1, 0, 0]
    >>> daily_temperatures([30, 40, 50, 60])
    [1, 1, 1, 0]
    >>> daily_temperatures([30, 60, 90])
    [1, 1, 0]
    >>> daily_temperatures([90, 80, 70])
    [0, 0, 0]
    >>> daily_temperatures([])
    []
    """
    answer = [0] * len(temperatures)
    stack: list[int] = []  # indices of days still waiting for a warmer day

    for day, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            colder_day = stack.pop()
            answer[colder_day] = day - colder_day
        stack.append(day)

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()