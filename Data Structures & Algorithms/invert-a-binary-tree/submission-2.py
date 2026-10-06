# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = deque([root])
        while stack:
            u = stack.popleft()
            u.left, u.right = u.right, u.left
            for v in [u.left, u.right]:
                if v: stack.append(v)        
        return root