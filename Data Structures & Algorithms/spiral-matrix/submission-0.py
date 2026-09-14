class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        final_mat = []
        while (left < right) and (top < bottom):
            for i in range(left, right):
                final_mat.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                final_mat.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                final_mat.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                final_mat.append(matrix[i][left])
            left += 1
        return final_mat