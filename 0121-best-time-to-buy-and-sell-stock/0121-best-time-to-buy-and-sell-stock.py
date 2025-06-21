class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     day1price, day2price = prices[0], prices[0]
    #     max_profit = 0
    #     for i in range(1, len(prices)):

    #         if prices[i] < day1price:
    #             day1price, day2price = prices[i], prices[i]
            
    #         else:

    #             if prices[i] > day2price:
    #                 day2price = prices[i]


    #             if day2price - day1price > max_profit:
    #                 max_profit = day2price - day1price

    #     return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        price_min = prices[0]
        profit_max = 0

        for price in prices:
            price_min = min(price_min, price)
            profit_max = max(profit_max, price-price_min)

        return profit_max

