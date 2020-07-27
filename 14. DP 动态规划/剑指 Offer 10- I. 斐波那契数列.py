# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        ppv = 0
        pv = 1
        for i in range(2, n+1):
            res = ppv + pv
            ppv = pv
            pv = res
        return res
