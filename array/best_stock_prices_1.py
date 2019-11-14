from typing import List


def max_profit(prices: List[int]) -> int:
    best_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > best_profit:
                best_profit = profit

    return best_profit


def max_profit(prices: List[int]) -> int:
    best_profit = 0
    min_price = 999

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > best_profit:
            best_profit = prices[i] - min_price
    return best_profit


print(max_profit([7,1,5,3,6,4]))