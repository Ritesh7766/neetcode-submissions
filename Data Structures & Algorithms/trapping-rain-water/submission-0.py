class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        mx = 0
        for h in height:
            mx = max(mx, h)
            left_max.append(mx)
        
        right_max = [0] * len(height)
        mx = 0
        for i in range(-1, -(len(height)+1), -1):
            mx = max(mx, height[i])
            right_max[i] = mx
        
        water = 0
        for i, h in enumerate(height):
            water += (min(
                left_max[i], right_max[i]    
            ) - h)
        return water
