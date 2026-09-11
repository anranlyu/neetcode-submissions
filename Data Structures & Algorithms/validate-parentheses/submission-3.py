class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pairs = {"(": ")", "[": "]", "{": "}"}
        for x in s:
            if x in pairs:
                stack.append(x)
            else:
                if not stack or x != pairs[stack.pop()]:
                    return False
        return len(stack) == 0
