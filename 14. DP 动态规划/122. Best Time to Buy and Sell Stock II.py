class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res
