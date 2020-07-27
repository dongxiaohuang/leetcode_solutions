# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""
        n = n % len(s)
        if not n:
            return s
        s = list(s)
        self.reverse(s, 0, len(s)-1)
        self.reverse(s, 0, len(s)-1-n)
        self.reverse(s, len(s)-n, len(s)-1)
        return ''.join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
