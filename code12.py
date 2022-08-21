def maxProfit(prices: list[int]) -> int:
    profit = 0
    min_value = prices[0]
    for price in prices:
        min_value = min(min_value, price)
        profit = max(profit, price - min_value)
    return profit
print(maxProfit([7,1,5,3,6,4]))