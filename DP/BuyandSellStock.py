"""121. Best Time to Buy and Sell Stock
IMPORTant, 5 levels of same question. read the solution

You are given an array prices where prices[i] is the 
    price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
    and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
"""


def maxprof(prices: list[int]) -> int:
    profit = 0
    for i, price in enumerate(prices):
        for price2 in prices[i+1:]:
            if profit<price2-price:
                profit = price2-price
    return profit

def maxpro(prices):
    n = len(prices)
    if n <= 1:
        return 0
    max_profit = 0
    min_price = prices[0]
    
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit



def maxprofit(prices: list[int]) -> int:
    maxDiff = 0
    n = len(prices)
    maxRight = prices[n - 1]

    for i in range(n - 2, -1, -1):
        if (prices[i] > maxRight):
            maxRight = prices[i]
        else:
            diff = maxRight - prices[i]
            if (diff > maxDiff):
                maxDiff = diff
    return maxDiff

print(maxpro([7,1,5,3,6,4]))
print(maxprof([7,1,5,3,6,4]))
print(maxprofit([7,1,5,3,6,4]))
print(maxpro([7,25,5,3,6,4,34,56,2,23]))
print(maxprof([7,25,5,3,6,4,34,56,2,23]))
print(maxprofit([7,25,5,3,6,4,34,56,2,23]))
print(maxpro([7,153,5,3,6,4,34,56,2,2535,46,56,42,53,521,4,25,46,23]))
print(maxprof([7,153,5,3,6,4,34,56,2,2535,46,56,42,53,521,4,25,46,23]))
print(maxprofit([7,153,5,3,6,4,34,56,2,2535,46,56,42,53,521,4,25,46,23]))