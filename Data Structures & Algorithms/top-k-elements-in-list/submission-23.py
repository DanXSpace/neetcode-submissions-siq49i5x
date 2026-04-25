class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        heap = []
        res = []

        for i, n in enumerate(nums):
            num_count[n] = num_count.get(n, 0) + 1
        
        for num, freq in num_count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
            
        for freq, num in heap:
            res.append(num)
        
        return res