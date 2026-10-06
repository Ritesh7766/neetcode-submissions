class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            key = target - num
            if key in mp:
                return [mp[key], i]
            mp[num] = i
