class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        freq = {}
        for i in s1:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        l = 0
        while l <= len(s2) - n:
            window = s2[l:n + l]
            freq_window = {}
            for j in window:
                if j not in freq_window:
                    freq_window[j] = 1
                else:
                    freq_window[j] += 1
            
            if freq_window == freq:
                return True
            
            else:
                l += 1
            
        return False
            
            