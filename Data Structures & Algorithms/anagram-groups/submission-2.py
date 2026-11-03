class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in strs:
            freq = [0] * 26

            for s in i:
                freq[ord(s) - ord('a')] += 1
            
            key = tuple(freq)
        
            if key not in groups:
                groups[key] = []
        
            groups[key].append(i)

        return list(groups.values())