class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2

        dp = [[False]*(target+1) for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                if dp[i][target]:
                    return True
        # print(dp)
        return dp[i][target]
