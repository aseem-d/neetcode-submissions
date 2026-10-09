class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map_s = {}
        freq_map_t = {}

        for i in s:
            if i not in freq_map_s:
                freq_map_s[i] = 1
            else:
                freq_map_s[i] += 1
        
        for j in t:
            if j not in freq_map_t:
                freq_map_t[j]= 1
            else:
                freq_map_t[j] += 1
        
        if freq_map_s == freq_map_t:
            return True
        else:
            return False