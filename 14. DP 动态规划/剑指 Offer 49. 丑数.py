# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        dp = [1]*index
        a, b, c = 0, 0, 0
        for i in range(1, index):
            da = dp[a]*2
            db = dp[b]*3
            dc = dp[c]*5
            num = min(da, db, dc)
            if num == da:
                a += 1
            if num == db:
                b += 1
            if num == dc:
                c += 1
            dp[i] = num
        return dp[-1]
