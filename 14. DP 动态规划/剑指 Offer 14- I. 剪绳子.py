# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, n):
        # write code here
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [1]*(n+1)
        dp[3] = 2
        for j in range(3, n+1):
            for i in range(j+1):
                dp[j] = max(dp[j], dp[j-i]*i)
        return dp[-1]
