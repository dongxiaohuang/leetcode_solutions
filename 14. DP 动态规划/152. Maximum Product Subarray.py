class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        maxP_till_now = nums[0]
        minP_till_now = nums[0]
        for i in range(1, len(nums)):
            _maxP_till_now = max(
                nums[i], nums[i]*maxP_till_now, nums[i]*minP_till_now)
            minP_till_now = min(
                nums[i], nums[i]*minP_till_now, nums[i]*maxP_till_now)
            maxP_till_now = _maxP_till_now
            res = max(res, maxP_till_now)
            print(minP_till_now, maxP_till_now)
        return res
