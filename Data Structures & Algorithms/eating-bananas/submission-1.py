from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_time(rate: int) -> int:
            total = 0
            for pile in piles:
                total += ceil(pile / rate)
            return total
        
        l, r = 1, max(piles)
        while l <= r:
            rate = (l + r) // 2
            time = total_time(rate)
            if time <= h:
                r = rate - 1
            else:
                l = rate + 1
        return l
