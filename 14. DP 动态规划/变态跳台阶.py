# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            for k in range(i):
                dp[i] += dp[k]

        # print(dp)
        return dp[-1]
