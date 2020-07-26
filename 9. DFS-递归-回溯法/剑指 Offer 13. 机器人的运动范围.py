# -*- coding:utf-8 -*-
class Solution:

    def movingCount(self, k, m, n):
        # write code here
        used = [[False]*n for i in range(m)]
        res = self.helper(k, m, n, 0, 0, used)
        return res

    def helper(self, k, m, n, i, j, used):
        if i < 0 or i >= m:
            return 0
        if j < 0 or j >= n:
            return 0
        r1, r2, r3, r4 = 0, 0, 0, 0
        if self.count_pos(i, j) <= k and not used[i][j]:
            used[i][j] = True
            # move right
            r1 = self.helper(k, m, n, i, j+1, used)
            # move left
            r2 = self.helper(k, m, n, i, j-1, used)
            # move up
            r3 = self.helper(k, m, n, i-1, j, used)
            # move down
            r4 = self.helper(k, m, n, i+1, j, used)
            return sum([r1, r2, r3, r4])+1
        return 0

    def count_pos(self, m, n):
        res = 0
        while m:
            res += m % 10
            m = m // 10
        while n:
            res += n % 10
            n = n // 10
        return res
