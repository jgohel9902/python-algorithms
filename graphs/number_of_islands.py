def num_islands(grid: list[list[str]]) -> int:
    """
    Given an m x n grid of '1's (land) and '0's (water), return
    the number of islands. An island is formed by connecting
    adjacent lands horizontally or vertically.

    Approach: DFS — for each unvisited land cell, trigger a DFS
    that marks all connected land cells as visited ('0').
    Count how many times DFS is triggered = number of islands.

    Time Complexity: O(m * n) — visit each cell at most once
    Space Complexity: O(m * n) — recursion stack in worst case

    Examples:
    >>> num_islands([
    ...     ["1","1","1","1","0"],
    ...     ["1","1","0","1","0"],
    ...     ["1","1","0","0","0"],
    ...     ["0","0","0","0","0"]
    ... ])
    1
    >>> num_islands([
    ...     ["1","1","0","0","0"],
    ...     ["1","1","0","0","0"],
    ...     ["0","0","1","0","0"],
    ...     ["0","0","0","1","1"]
    ... ])
    3
    >>> num_islands([["0","0","0"]])
    0
    >>> num_islands([["1"]])
    1
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)

    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")