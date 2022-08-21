def maxProfit(prices: list[int]) -> int:
    profit = [0,]
    min_value = prices[0]
    for i in range(len(prices)):
        min_value = min(prices[i], min_value)
        profit.append(prices[i] - min_value)
    return max(profit)
print(maxProfit([7,1,5,3,6,4]))