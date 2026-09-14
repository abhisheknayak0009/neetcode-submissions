class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                index, value = stack.pop()
                res = max(res, value * (i - index))
            stack.append([index, heights[i]])
        while stack:
            index, value = stack.pop()
            res = max(res, value * (len(heights) - index))
        return res