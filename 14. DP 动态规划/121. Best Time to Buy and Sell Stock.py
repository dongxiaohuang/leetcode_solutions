class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price_so_far = prices[0]
        res = 0
        for i in range(1, len(prices)):
            min_price_so_far = min(prices[i], min_price_so_far)
            res = max(res, prices[i]-min_price_so_far)

        return res
