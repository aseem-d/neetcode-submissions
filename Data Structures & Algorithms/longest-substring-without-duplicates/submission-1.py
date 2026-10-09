class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            longest = max(longest, r - l +1)
        
        return longest

            

