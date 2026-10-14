class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []
        l = 0
        r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                combined += [nums1[l]]
                l += 1
            else:
                combined += [nums2[r]]
                r += 1
        
        while l < len(nums1):
            combined += [nums1[l]]
            l += 1

        while r < len(nums2):
            combined += [nums2[r]]
            r += 1

        n = len(combined)  
        

        if n % 2 != 0:
            m = int((n-1) / 2)
            return combined[m]
        else:
            m1 = int(n/2)
            m2 = int((n/2) - 1)
            return (combined[m1] + combined[m2]) / 2