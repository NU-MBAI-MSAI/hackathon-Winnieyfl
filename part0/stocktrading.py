"""
Authors: Winnie Li, Ritwik Chakradhar
Creation date: 09/03/2025
Stock trading - return the biggest profit
"""

def maxProfit(prices):
    # if list is empty, return 0
    if not prices:
        return 0
    # variable for maximum profit
    global_max = 0
    for buy in range(len(prices)):
        for sell in range(buy, len(prices)):
            # for each date, and each subsequent days, calculate potential profit
            diff = prices[sell] - prices[buy]
            # calculate the maximum profit
            global_max = max(global_max, diff)
    return global_max



if __name__ == "__main__":
   prices = [7,6,4,3,1]
   print(maxProfit(prices))