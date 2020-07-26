# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        right_start = 0
        while sequence[right_start] < root:
            right_start += 1

        for i in range(right_start, len(sequence)-1):
            if sequence[i] < root:
                return False
        left_res = True
        right_res = True

        left_sequence = sequence[:right_start]
        right_sequence = sequence[right_start:len(sequence)-1]
        if left_sequence:
            left_res = self.VerifySquenceOfBST(left_sequence)
        if right_sequence:
            right_res = self.VerifySquenceOfBST(right_sequence)
        return left_res and right_res
