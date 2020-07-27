class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        dp = [1]*len(nums)
        dp[0] = 1
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        stack = [nums[0]]
        for i in nums[1:]:
            if stack[-1] < i:
                stack.append(i)
            else:
                pos = bisect.bisect_left(
                    stack, i, 0, len(stack))  # Binary seacrh
                stack[pos] = i
        return len(stack)
