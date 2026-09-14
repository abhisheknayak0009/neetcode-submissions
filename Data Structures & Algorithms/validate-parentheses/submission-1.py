class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in range(len(s)):
            if s[i] not in hashMap:
                stack.append(s[i])
                continue
            if not stack or stack[-1] != hashMap[s[i]]:
                return False
            stack.pop()
        return stack == []