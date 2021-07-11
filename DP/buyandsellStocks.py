"""121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5



Efficient approach: If we are allowed to buy and sell only once, then we can use following algorithm. Maximum difference between two elements. Here we are allowed to buy and sell multiple times. 


Find the local minima and store it as starting index. If not exists, return.
Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
Update the solution (Increment count of buy sell pairs)
Repeat the above steps if end is not reached.
"""
# 1. naive aproach
# 2. just find curr min price and maxprof
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        cost = 0
        maxcost = 0
        if (n == 0):
            return 0
        
        min_price = prices[0]
        
        for i in range(n):
            min_price = min(min_price, prices[i])
            cost = prices[i] - min_price
            maxcost = max(maxcost, cost)
        return maxcost


# Like min element, we can also keep track of max element from right side.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
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


"""
3. First find the difference between the adjacent elements of the array and 
   store all differences in an auxiliary array diff[] of size n-1. 
Now this problems turns into finding the maximum sum subarray of this difference array."""
# least fast of all three, takes more memory too

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0
        diff = [0] * (n - 1)
        for i in range (0, n-1):
            diff[i] = prices[i+1] - prices[i]

        # Now find the maximum sum
        # subarray in diff array
        
        max_diff = diff[0]
        for i in range(1, n-1):
            if (diff[i-1] > 0):
                diff[i] += diff[i-1]

            if (max_diff < diff[i]):
                max_diff = diff[i]
        if max_diff<0:
            return 0
        return max_diff


# same aproach but less space, O(1) actually
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0
        diff = prices[1] - prices[0]
        curr_sum = diff
        max_sum = curr_sum
        for i in range(1, n - 1):
            diff = prices[i + 1] - prices[i]
            if (curr_sum > 0):
                curr_sum += diff
            else:
                curr_sum = diff
            if (curr_sum > max_sum):
                max_sum = curr_sum
        if max_sum<=0:
            return 0
        return max_sum

