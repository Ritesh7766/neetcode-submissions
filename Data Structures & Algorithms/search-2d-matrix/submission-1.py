class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        
        """
        l, r = 0, len(matrix) - 1
        row = None
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif matrix[m][0] < target:
                l += 1
            else:
                r -= 1

        if row is None: return False
        arr = matrix[row]
        l, r = 0, len(arr)
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l += 1
            else:
                r -= 1
        return False
