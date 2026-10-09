class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        position = 0
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            x = target - nums[i]
            if x not in hash_map:
                hash_map[x] = position
                position += 1



        
