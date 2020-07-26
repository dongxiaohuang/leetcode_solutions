# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        end = (tsum+1)//2
        res = []
        for j in range(2, end+1):
            consume = True
            for i in range(1, j):
                if consume:
                    tmp = ((i+j)*(j-i+1))/2
                    if tmp == tsum:
                        res.append(list(range(i, j+1)))
                    elif tmp > tsum:
                        continue
                    else:
                        consume = False
                else:
                    break
        return res
