from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k1, k2 = Counter(s), Counter(t)
        return k1 == k2
