class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize a var for profit
        profit = 0
        # check edge case -- if length is one then max profit is 0
        if len(prices) == 1:
            return profit
        # main body, initialize when to buy and sell.
        # basically buy is left pointer and sell is right pointer
        buy, sell = 0, 1
        # so while right pointer hasn't reached the end
        while sell < len(prices):
            # if we can sell for a profit, we keep the buy at the same price and compare if current profit is bigger
            # and we continue progress sell pointer until when we reach a lower price than the current buy
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
            # when that happens, we move the buy there and have sell be the price immediately to the right of the new buy, and then the while loop does the comparison again 
            else:
                buy = sell
                sell = buy + 1
        return profit

        