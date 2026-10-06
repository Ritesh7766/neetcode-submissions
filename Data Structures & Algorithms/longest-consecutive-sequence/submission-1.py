from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set(nums)
        visited = set()

        def dfs(node):
            n = 0
            stack = deque([node])

            while stack:
                u = stack.pop()
                visited.add(u)
                n += 1
                for v in [u - 1, u + 1]:
                    if v in exists and v not in visited:
                        stack.append(v)
            return n
        
        mx = 0
        for num in nums:
            mx = max(mx, dfs(num))
        return mx
