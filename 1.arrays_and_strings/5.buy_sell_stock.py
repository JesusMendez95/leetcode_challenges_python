""" 121. Best Time to Buy and Sell Stock
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104 """

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min, max, profit, last_value = 0, 0, 0, prices[0]
        for i in range(len(prices)):
            if prices[i] > last_value:
                max = i
                if min < max and (prices[max] - prices[min]) > profit:
                    profit = prices[max] - prices[min]
            elif prices[i] < prices[min]:
                min = i
            last_value = prices[i]  
        return profit
    # def maxProfit(self, prices: List[int]) -> int:
    #     min = 0
    #     for i in range(len(prices)):
    #         for j in range(i+1,len(prices)):
    #             if prices[i] < prices[j] and prices[i] - prices[j] < min:
    #                 min = prices[i] - prices[j]
    #     return abs(min)

#-----------------------------COMPLEXITY ANALYSIS--------------------------------

import time
import random
import matplotlib.pyplot as plt

class Solution:
    def maxProfit(self, prices):
        min_value = prices[0]
        profit = 0
        for value in prices:
            if value > min_value:
                if value - min_value > profit:
                    profit = value - min_value
            elif value < min_value:
                min_value = value
        return profit

# Function to measure time taken for different input sizes
def measure_time(n):
    prices = [random.randint(0, 10**4) for _ in range(n)]  # Generate random prices
    solution = Solution()
    start_time = time.time()
    solution.maxProfit(prices)
    return time.time() - start_time  # Execution time in seconds

# Test different input sizes
input_sizes = [10**3, 10**4, 10**5, 10**6]
execution_times = [measure_time(n) for n in input_sizes]

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b', label="Execution Time")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Time Complexity Analysis of maxProfit()")
plt.grid(True)
plt.legend()
plt.show()


#--------------------------------------- SPACE ---------------------------------------------------

import sys
import numpy as np

# Function to measure memory usage for different input sizes
def measure_memory(n):
    prices = [random.randint(0, 10**4) for _ in range(n)]  # Generate random prices
    solution = Solution()
    
    # Measure memory usage of key variables
    prices_size = sys.getsizeof(prices) + sum(sys.getsizeof(x) for x in prices)  # List + elements
    solution_size = sys.getsizeof(solution)  # Object instance
    total_memory = prices_size + solution_size
    
    return total_memory / 1024  # Convert to KB

# Test different input sizes
memory_usage = [measure_memory(n) for n in input_sizes]

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(input_sizes, memory_usage, marker='o', linestyle='-', color='r', label="Memory Usage")
plt.xlabel("Input Size (n)")
plt.ylabel("Memory Usage (KB)")
plt.title("Space Complexity Analysis of maxProfit()")
plt.grid(True)
plt.legend()
plt.show()
