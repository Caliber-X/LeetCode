import heapq

class Solution:

    # # heap (time_complexity=O(nlogn))
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    #     frequency_dict = {}
    #     for i in nums:
    #         frequency_dict[i] = 1 + frequency_dict.get(i, 0)
        
    #     # heap = []
    #     # for val, freq in frequency_dict.items():
    #     #     heapq.heappush(heap, (-freq, val))

    #     # output = []
    #     # for i in range(k):
    #     #     freq, val = heapq.heappop(heap)
    #     #     output.append(val)

    #     output = heapq.nlargest(k, frequency_dict.keys(), key=frequency_dict.get)

    #     return output

    # bucket sort (time_complexity=O(n))
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict = {}
        for i in nums:
            frequency_dict[i] = 1 + frequency_dict.get(i, 0)
        
        bucket = [None] * len(nums)
        for val, freq in frequency_dict.items():
            freq -= 1
            if bucket[freq] is None:
                bucket[freq] = []
            bucket[freq].append(val)
        
        output = []
        count = 0
        for values in reversed(bucket):
            if values is None:
                continue
            output.extend(values)
            count += len(values)
            if count == k:
                break

        return output
