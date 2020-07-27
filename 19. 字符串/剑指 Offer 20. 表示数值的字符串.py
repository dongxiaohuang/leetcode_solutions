# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sign = False
        self.hasE = False
        self.has_dcm = False
    def isNumeric(self, s):
        for i in range(len(s)):
            char = s[i]
            if char == 'e' or char == 'E':
                if self.hasE:
                    return False
                if i == len(s)-1:
                    return False
                self.hasE = True
            elif char == '+' or char == '-':
                # only can be after e
                if not self.sign:
                    if i == 0:
                        continue
                    else:
                        if s[i-1] not in ['e', 'E']:
                            return False
                sign = True
            elif char == '.':
                if self.has_dcm:
                    return False
                if self.hasE:
                    return False
                self.has_dcm = True
            elif char < '0' or char > '9':
                return False

        return True