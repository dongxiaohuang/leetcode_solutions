class Solution:
    def myAtoi(self, str: str) -> int:
        if str == '': return 0

        res = 0
        start = 0
        while start < len(str) and str[start] == ' ':
            start += 1
        sign = 1
        for idx, char in enumerate(str[start:]):
            if idx == 0 and char == '-':
                sign = -1
            elif idx == 0 and char == '+':
                continue
            else:
                if char >= '0' and char <= '9':
                    res = res*10 + int(char)
                else:
                    break
        tmp_res = sign * res
        if tmp_res > pow(2, 31)-1:
            return pow(2, 31)-1
        if tmp_res < -pow(2, 31):
            return -pow(2, 31) 
        return tmp_res