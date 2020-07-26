class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        res_so_far = nums[0]
        for i in range(1, len(nums)):
            res_so_far = max(nums[i],  nums[i]+res_so_far)
            res = max(res, res_so_far)
        return res
