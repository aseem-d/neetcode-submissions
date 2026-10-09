class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prod_arr[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums)-1, -1, -1):
            prod_arr[i] *= suffix
            suffix *= nums[i]

        return prod_arr





            


