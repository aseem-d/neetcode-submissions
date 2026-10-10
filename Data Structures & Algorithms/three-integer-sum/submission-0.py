class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums_asc = sorted(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums_asc[i] == nums_asc[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums_asc[i] + nums_asc[l] + nums_asc[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums_asc[i], nums_asc[l], nums_asc[r]])
                    l += 1
                    r -= 1
                    while l < r and nums_asc[l] == nums_asc[l-1]:
                        l += 1
                    while l < r and nums_asc[r] == nums_asc[r+1]:
                        r -= 1

        return result

        

        