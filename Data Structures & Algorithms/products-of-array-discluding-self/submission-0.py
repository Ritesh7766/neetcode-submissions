class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1, 2, 4, 6
        
        1, 1, 2, 8
        48, 24, 6, 1
         
        48, 24
        """
        pre_prod, post_prod = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            pre_prod[i] = pre_prod[i - 1] * nums[i - 1]
        
        for i in range(-2, -len(nums)-1, -1):
            post_prod[i] = post_prod[i + 1] * nums[i + 1]

        return [
            pre_prod[i] * post_prod[i]
            for i in range(len(nums))
        ]
