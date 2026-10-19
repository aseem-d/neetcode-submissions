class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        digits[-1] = 0
        
        if n == 1:
            return [1,0]
        
        result = self.plusOne(digits[:-1])
        result.append(0)

        return result
        