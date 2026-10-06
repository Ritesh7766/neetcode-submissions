from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [(-cnt, num) for num, cnt in Counter(nums).items()]
        heapq.heapify(freq)
        return [heapq.heappop(freq)[-1] for _ in range(k)]

