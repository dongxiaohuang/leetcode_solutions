class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        max_no_share = 0
        max_hold_share = 0
        for i in range(1, len(prices)):
            max_no_share, max_hold_share = max(max_no_share, max_hold_share+prices[i]-prices[i-1]-fee), max(
                max_no_share, max_hold_share + prices[i]-prices[i-1])
        return max_no_share