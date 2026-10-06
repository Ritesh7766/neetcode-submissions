import numpy as np


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(w):00200}{w}" for w in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0

        while idx < len(s):
            n = int(s[idx:idx + 200])
            idx += 200               
            res.append(s[idx:idx + n])
            idx += n                 

        return res
