# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, a):
        # write code here
        b = [1]*len(a)
        for i in range(1, len(a)):
            b[i] = b[i-1]*a[i-1]

        tmp = 1
        for j in range(len(a)-2, -1, -1):
            tmp = tmp*a[j+1]
            b[j] = b[j]*tmp

        return b
        