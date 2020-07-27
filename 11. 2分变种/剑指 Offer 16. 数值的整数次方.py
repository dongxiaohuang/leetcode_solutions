class Solution:
    def myPow(self, x: float, n: int) -> float:
        tmp = 1
        if n < 0:
            x = 1 / x
            n *= -1
        while n:
            if n & 1:
                tmp *= x
            x *= x
            n >>= 1
        return tmp
