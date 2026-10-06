from collections import deque, defaultdict
import heapq
from math import inf

class MinStack:

    def __init__(self):
        self._stack = deque()
        self._freq = defaultdict(int)
        self._cur_min = inf

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._freq[val] += 1
        self._cur_min = min(self._cur_min, val)

    def pop(self) -> None:
        val = self._stack.pop()
        self._freq[val] -= 1
        if val == self._cur_min and self._freq[val] == 0:
            self._cur_min = min(self._stack) if self._stack else inf

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]

    def getMin(self) -> int:
        return self._cur_min
        
