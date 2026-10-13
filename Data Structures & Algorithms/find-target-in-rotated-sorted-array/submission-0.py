class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = {}
        for i in range(len(nums)):
            idx[nums[i]] = i
        
        max = float('-inf')

        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]

        max_idx = idx[max]

        if max_idx == len(nums) - 1:
            nums_asc = nums
        else:
            nums_asc = nums[max_idx + 1:] + nums[:max_idx + 1]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums_asc[m] == target:
                return idx[nums_asc[m]]
            elif nums_asc[m] < target:
                l = m + 1
            else:
                r = m - 1

        return (-1)
        

        