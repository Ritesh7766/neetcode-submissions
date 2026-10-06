from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        comp = {"]":"[", "}":"{", ")":"("}
        stack = deque()
        for ch in s:
            if ch in ["[", "{", "("]:
                stack.append(ch)
            else:
                if stack and (stack[-1] == comp.get(ch)):
                    _ = stack.pop()
                else:
                    stack.append(ch)
        return False if len(stack) != 0 else True
