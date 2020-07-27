class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # method 1
        # import heapq
        # minq = []
        # for num in nums:
        #     if len(minq) < k:
        #         heapq.heappush(minq, num)
        #     else:
        #         topk = minq[0]
        #         if num > topk:
        #             heapq.heappop(minq)
        #             heapq.heappush(minq, num)
        # return minq[0]

        # partition
        if len(nums) == 1:
            return nums[0]
        target_k = len(nums) - k
        start = 0
        end = len(nums)-1

        while start <= end:
            idx_k = self.partition(nums, start, end)
            if idx_k == target_k:
                return nums[idx_k]
            elif idx_k < target_k:
                start = idx_k+1
            else:
                end = idx_k-1

    def partition(self, nums, start, end):
        pivot = nums[end]
        slow = fast = start

        while fast < end:
            if nums[fast] <= pivot:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
        nums[slow], nums[end] = nums[end], nums[slow]
        return slow
