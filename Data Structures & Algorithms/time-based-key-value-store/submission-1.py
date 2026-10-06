from collections import defaultdict

class TimeMap:
    """
    [(1, "h"), (3, "s")]
    """
    def __init__(self):
        self._mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        history = self._mp.get(key, [])
        l, r = 0, len(history) - 1
        while l <= r:
            m = (l + r) // 2
            time, state = history[m]
            if time <= timestamp:
                l = m + 1
            else:
                r = m - 1
        if r >= 0:
            return history[r][-1]
        return ""