class Solution:
    def findMin(self, nums: List[int]) -> int:
        max = float('-inf')
        idx = {}
        for i in range(len(nums)):
            idx[nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]

        if idx[max] == len(nums) - 1:
            return nums[0]
        else:
            return nums[idx[max] + 1]

        
        
