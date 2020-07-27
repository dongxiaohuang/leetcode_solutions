class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n != 0:
            count += 1
            n = n & (n-1)
            print(n)
        return count
