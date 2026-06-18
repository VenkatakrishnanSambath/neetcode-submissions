from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        frequency_map = sorted(frequency_map, key = lambda x: frequency_map[x], reverse = True)
        return list(frequency_map[:k])
        