# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 1:
            return number
        elif number == 2:
            return 2
        pv = 2
        ppv = 1
        for i in range(number-2):
            res = pv+ppv
            ppv = pv
            pv = res
        return res
