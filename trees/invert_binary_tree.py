"""Invert Binary Tree: swap the left and right child of every node."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def to_list(root: TreeNode | None) -> list[int | None]:
    """
    Level-order list of the tree, with None for missing children (trailing Nones dropped).

    >>> to_list(None)
    []
    >>> to_list(TreeNode(1, TreeNode(2), TreeNode(3)))
    [1, 2, 3]
    >>> to_list(TreeNode(1, None, TreeNode(3)))
    [1, None, 3]
    """
    if root is None:
        return []
    result: list[int | None] = []
    queue: deque[TreeNode | None] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def invert_recursive(root: TreeNode | None) -> TreeNode | None:
    """
    >>> tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    >>> to_list(invert_recursive(tree))
    [4, 7, 2, 9, 6, 3, 1]
    >>> to_list(invert_recursive(TreeNode(1, TreeNode(2), None)))
    [1, None, 2]
    >>> to_list(invert_recursive(TreeNode(1)))
    [1]
    >>> invert_recursive(None) is None
    True
    """
    if root is None:
        return None
    root.left, root.right = invert_recursive(root.right), invert_recursive(root.left)
    return root


def invert_iterative(root: TreeNode | None) -> TreeNode | None:
    """
    >>> tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    >>> to_list(invert_iterative(tree))
    [4, 7, 2, 9, 6, 3, 1]
    >>> to_list(invert_iterative(TreeNode(1, None, TreeNode(2))))
    [1, 2]
    >>> invert_iterative(None) is None
    True
    """
    if root is None:
        return None
    queue: deque[TreeNode] = deque([root])
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root


if __name__ == "__main__":
    import doctest

    doctest.testmod()