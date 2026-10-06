from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for wrd in strs:
            k = [0] * 26
            for ch in wrd:
                k[ord(ch) - 97] += 1
            mp[tuple(k)].append(wrd)
        return list(mp.values())
