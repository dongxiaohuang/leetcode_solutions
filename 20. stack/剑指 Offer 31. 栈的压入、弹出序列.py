# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV and not popV:
            return True
        if len(pushV) != len(popV):
            return False
        stack = []
        for val in pushV:
            stack.append(val)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if stack:
            return False
        return True