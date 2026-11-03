class Solution:
    def findMin(self, nums: List[int]) -> int:
        max_idx = 0
        max = -1000
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                max_idx = i
        

        array_srt = nums[max_idx+1:] + nums[:max_idx+1]

        return array_srt[0]