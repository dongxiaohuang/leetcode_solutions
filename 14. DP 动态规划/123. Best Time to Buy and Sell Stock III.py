class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        p1 = [0]*len(prices)
        p2 = [0]*len(prices)
        min_so_far = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            p1[i] = max(max_profit, prices[i] - min_so_far)

            if prices[i] < min_so_far:
                min_so_far = prices[i]
            if p1[i] > max_profit:
                max_profit = p1[i]

        max_profit = 0
        max_so_far = prices[-1]
        for j in range(len(prices)-1, -1, -1):
            p2[j] = max(max_profit, max_so_far - prices[j])
            if p2[j] > max_profit:
                max_profit = p2[j]
            if max_so_far < prices[j]:
                max_so_far = prices[j]

        res = 0
        for i in range(len(prices)):
            res = max(res, p1[i]+p2[i])
        return res
