class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums_asc = sorted(nums)
        longest = 1
        curr = 1
        i = 1
        while i < (len(nums)):
            if nums_asc[i] - nums_asc[i-1] == 1:
                curr += 1
                i += 1
                if curr > longest:
                    longest = curr
            elif nums_asc[i] == nums_asc[i-1]:
                i += 1    
            else:
                curr = 1
                i += 1

        return longest
