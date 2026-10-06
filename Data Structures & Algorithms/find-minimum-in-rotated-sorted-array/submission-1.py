from math import inf

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mn = inf
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                mn = min(mn, nums[l])
                l = m + 1
            else:
                mn = min(mn, nums[m])
                r = m - 1
        return mn