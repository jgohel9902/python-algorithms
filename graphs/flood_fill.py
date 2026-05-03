def flood_fill(
    image: list[list[int]], sr: int, sc: int, color: int
) -> list[list[int]]:
    """
    Given an image as a 2D array, a starting pixel (sr, sc) and a
    new color, flood fill from the starting pixel. Change the color
    of the starting pixel and all 4-directionally connected pixels
    of the same original color to the new color.

    Approach: DFS from starting pixel, recursively fill all
    connected pixels that match the original color.

    Time Complexity: O(m * n) — visit each pixel at most once
    Space Complexity: O(m * n) — recursion stack worst case

    Examples:
    >>> flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
    [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    >>> flood_fill([[0,0,0],[0,0,0]], 0, 0, 0)
    [[0, 0, 0], [0, 0, 0]]
    >>> flood_fill([[0,0,0],[0,1,1]], 1, 1, 1)
    [[0, 0, 0], [0, 1, 1]]
    """
    original_color = image[sr][sc]

    if original_color == color:
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original_color:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")