class Solution:
    def isHappy(self, n: int) -> bool:
        
        flag = False

        while not flag:
            sum_square = 0
            digits = [int(d) for d in str(n)]
            for i in digits:
                sum_square += (i**2)
            
            n = sum_square

            if sum_square == 1:
                flag = True
            if sum_square == 4:
                return False
        
        return flag
        