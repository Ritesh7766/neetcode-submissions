

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        k1, k2 = [0] * 26, [0] * 26
        for c1, c2 in zip(s, t):
            k1[ord(c1) - 97] += 1
            k2[ord(c2) - 97] += 1
        return tuple(k1) == tuple(k2)
