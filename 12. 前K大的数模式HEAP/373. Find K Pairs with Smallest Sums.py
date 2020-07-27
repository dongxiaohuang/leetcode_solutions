class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        maxheap = []
        import heapq
        i = 0
        for num1 in nums1:
            for num2 in nums2:
                if i < k:
                    heapq.heappush(maxheap, (-(num1+num2), [num1, num2]))
                    i += 1
                else:
                    k_min, [n1, n2] = maxheap[0]
                    print(-k_min)
                    if num1+num2 < -k_min:
                        heapq.heappop(maxheap)
                        heapq.heappush(maxheap, (-(num1+num2), [num1, num2]))

        return [v for k, v in maxheap]
