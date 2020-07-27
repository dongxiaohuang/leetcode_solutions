class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 3 or len(nums) == 2:
            return max(nums)

        pprev = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)-1):
            cur = max(pprev+nums[i], prev)
            pprev = prev
            prev = cur
        max1 = cur

        pprev = nums[1]
        prev = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            cur2 = max(pprev + nums[i], prev)
            pprev = prev
            prev = cur2
        max2 = cur2
        return max(max1, max2)
