class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = []

        rows = len(matrix)
        columns = len(matrix[0])

        for row in range(rows):
            flat_matrix += matrix[row]

        l = 0
        r = (rows * columns) - 1

        while l <= r:
            m = (l+r)//2
            if flat_matrix[m] == target:
                return True
            elif flat_matrix[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
            
            