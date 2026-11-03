class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []

        rows = len(matrix)
        columns = len(matrix[0])

        for row in range(rows):
            flat += matrix[row]
        l = 0
        r = (rows*columns) - 1

        while l <= r:
            m = (l+r)//2
            if flat[m] == target:
                return True
            elif flat[m] < target:
                l += 1
            else:
                r -= 1
        
        return False
            