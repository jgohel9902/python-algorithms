def exist(board: list[list[str]], word: str) -> bool:
    """
    Given an m x n grid of characters and a word, return True if
    the word exists in the grid. Word can be constructed from
    sequentially adjacent cells (horizontal or vertical).
    The same cell cannot be used more than once.

    Approach: Backtracking DFS — try each cell as starting point,
    explore all 4 directions recursively, mark visited cells
    temporarily and restore after backtracking.

    Time Complexity: O(m * n * 4^len(word))
    Space Complexity: O(len(word)) — recursion stack depth

    Examples:
    >>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True
    >>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    True
    >>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    False
    >>> exist([["a"]], "a")
    True
    """
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (
            dfs(r + 1, c, idx + 1)
            or dfs(r - 1, c, idx + 1)
            or dfs(r, c + 1, idx + 1)
            or dfs(r, c - 1, idx + 1)
        )

        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")