class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -4, -1, -1, 0, 1, 2

        -4, 
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[l] + nums[r] + target
                if sm == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sm < 0:
                    l += 1
                else:
                    r -= 1
        return res