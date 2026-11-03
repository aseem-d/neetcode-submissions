class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            
            freq_map[i] += 1

        asc_freq = sorted(list(freq_map.values()))

        top_k_slice = asc_freq[-k:]

        result = []

        for j in freq_map:
            if freq_map[j] in top_k_slice:
                result.append(j)

        return result