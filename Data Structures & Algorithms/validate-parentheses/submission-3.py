class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {}
        bracketMap = {'}': '{', ')': '(', ']': '['}
        stack = []

        for i in range(len(s)):
            if s[i] not in bracketMap:
                stack.append(s[i])
                continue
            if not stack or stack[-1] != bracketMap[s[i]]:
                return False
            stack.pop()
        return stack == [] 