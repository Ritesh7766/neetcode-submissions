# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(r):
            if not r: return 0
            queue = deque([(r, 1)])
            depth = 1
            while queue:
                u, depth = queue.popleft()

                for v in [u.left, u.right]:
                    if v: queue.append((v, depth + 1))
            return depth
        
        return bfs(root.left) + bfs(root.right)