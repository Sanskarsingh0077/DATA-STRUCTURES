class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        top , bottom = 0 , row - 1

        while top <= bottom: # Binary Search Cols to get target row in which target val is Present --> O(logm)
            row = (top + bottom) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                break

            if target > matrix[row][-1]:
                top = row + 1

            else:
                bottom = row - 1

        if not (top <= bottom):
            return False

        target_row = (top + bottom)//2
        l, r = 0 , col - 1

        while l <= r: # Binary Search row for target Value O(logn)
            mid = (l + r)//2 

            if target == matrix[target_row][mid]:
                return True

            if target > matrix[target_row][mid]:
                l = mid + 1

            else:
                r = mid - 1

        return False

        # TC : O(logm + logn)

            