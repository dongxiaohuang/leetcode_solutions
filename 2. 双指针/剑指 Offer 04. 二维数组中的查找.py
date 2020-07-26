# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = 0
        col = len(array[0])-1
        while row < len(array) and col >= 0:
            if array[row][col] == target:
                return True
            
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
                