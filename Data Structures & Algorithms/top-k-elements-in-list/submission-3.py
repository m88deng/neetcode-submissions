class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements
        # iterate through nums to track freq

        # top k most freq means removing len(unique elements - k)
        #priority queue
        import heapq

        from collections import defaultdict

        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        min_heap = [(freq, num) for num, freq in d.items()]

        heapq.heapify(min_heap)

        remove = len(min_heap) - k

        for i in range(remove):
            heapq.heappop(min_heap)  

        res = []
        
        for i in range(len(min_heap)):
            res.append(heapq.heappop(min_heap)[1])

        return res
