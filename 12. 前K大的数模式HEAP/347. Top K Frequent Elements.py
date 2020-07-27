class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        top_k = k
        # counter = [(k,v) for k,v in counter.items()]
        # counter = sorted(counter, key= lambda x: -x[1])
        # return [c[0] for c in counter[:(k)]]
        import heapq
        minheap = []
        for i, (k, v) in enumerate(counter.items()):
            if i < top_k:
                heapq.heappush(minheap, (v, k))
            else:
                _v, _k = minheap[0]
                if v > _v:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, (v, k))
            # print(minheap)
        return [k for v, k in minheap]
