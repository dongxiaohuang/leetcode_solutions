from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sw = deque()
        for i in range(k):
            while sw and nums[i] > nums[sw[-1]]:
                sw.pop()
            sw.append(i)
        ans = []
        for i in range(k, n):
            ans.append(nums[sw[0]])

            while sw and sw[0] <= i-k:
                sw.popleft()
            while sw and nums[i] > nums[sw[-1]]:
                sw.pop()
            sw.append(i)

        ans.append(nums[sw[0]])
        return ans
