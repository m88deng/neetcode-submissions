class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #min heap queue
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        queue = [(count, num) for num, count in freq.items()]
        heapq.heapify(queue)
        res = []
        for i in range(len(queue) - k):
            heapq.heappop(queue)[1]
        while(queue):
            res.append(heapq.heappop(queue)[1])
        return list(res)
        
        
        
        
      