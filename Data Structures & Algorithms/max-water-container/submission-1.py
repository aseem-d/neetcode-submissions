class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        curr_max = 0
        while l <= r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            if area >= curr_max:
                if curr_max == 0:
                    curr_max += area
                else:
                    curr_max = area
                
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return curr_max