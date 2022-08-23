def maxProfit(prices: list[int]) -> int:
    profit = 0
    min_value = prices[0]
    for price in prices:
        min_value = min(min_value, price)
        profit = max(profit, price - min_value)
    return profit
def max_profit(prices: list[int]) -> int:
    profit = 0
    before_price = prices[0]
    for price in prices[1:]:
        if before_price < price:
            profit += price - before_price
        before_price = price
    return profit
print(maxProfit([7,1,5,3,6,4]))
print(max_profit([7,1,5,3,6,4]))
