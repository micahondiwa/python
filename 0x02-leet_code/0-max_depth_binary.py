""" Given the root of a binary tree, return its maximum depth."""
def maxdepth(root):
    if root == Node:
        return 0
    left = 1
    right = 1
    if root.left:
        left = maxdepth(root.left)
    if root.right:
        right = maxdepth(root.right)
    return max(left, right)