# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, n):
        # write code here
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 2
        pprev = 1
        for i in range(3, n+1):
            res = prev+pprev
            pprev = prev
            prev = res
        return res
