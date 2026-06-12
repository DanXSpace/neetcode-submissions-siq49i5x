class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        r, c = len(matrix), len(matrix[0])

        left = 0
        right = (r * c) - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // c
            col = mid % c

            current_value = matrix[row][col]

            if current_value == target:
                return True
            elif current_value < target:
                left  = mid + 1
            else:
                right = mid - 1
        return False