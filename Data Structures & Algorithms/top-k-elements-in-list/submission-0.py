class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1

        freq = sorted((list(freq_map.values())))
        top_k_slice = freq[-k:]
        top_k = []
        for i in freq_map:
            if freq_map[i] in top_k_slice:
                top_k.append(i)
        
        return top_k
