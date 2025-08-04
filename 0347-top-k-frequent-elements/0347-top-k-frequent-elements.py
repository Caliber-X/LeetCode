import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict = {}
        for i in nums:
            frequency_dict[i] = 1 + frequency_dict.get(i, 0)
        
        heap = []
        for val, freq in frequency_dict.items():
            heapq.heappush(heap, (-freq, val))

        output = []
        for i in range(k):
            freq, val = heapq.heappop(heap)
            output.append(val)

        return output
