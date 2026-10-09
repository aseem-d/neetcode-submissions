class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}
        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                return True
        
        return False
        