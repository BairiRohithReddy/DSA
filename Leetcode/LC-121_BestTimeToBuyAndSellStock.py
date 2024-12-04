from typing import Optional, List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # in this approach we shall calculate profit if we purchase on a day prior to this day and then finally return the max profit of a day in the week 
        # initially lets assume the min_price as the price on day-1
        min_price = prices[0]
        # now if we buy and sell on the same day our profit will be 0 so initial profit be 0
        profit = 0
        for i in range(1, len(prices)):
            # now lets us calculate temporary profit on each day assuming we bought the stock on the previous min_price
            temp_profit = prices[i] - min_price
            profit = max(temp_profit, profit)
            # now the profit will store the max profit over the week
            # now we should also check if the present day price is less than the previous min_price if so then we replace min_price with todays price
            min_price = min(min_price, prices[i])
        # now we return the profit    
        return profit
        pass
        