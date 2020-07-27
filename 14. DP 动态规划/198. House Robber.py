class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        pprev = nums[0]
        prev = max(nums[0], nums[1])
        res = prev
        for i in range(2, len(nums)):
            cur = max(prev, nums[i]+pprev)
            res = max(cur, res)
            pprev = prev
            prev = cur
        return res
