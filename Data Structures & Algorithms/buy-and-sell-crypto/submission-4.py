class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10, 1, 5, 6, 7, 1]

        max_profit = 0
        left, right = 0, 1

        while right != len(prices):
            if prices[left] < prices[right]:
                price = prices[right] - prices[left]
                max_profit = max(max_profit, price)
            else:
                left = right
            right += 1
        return max_profit
        