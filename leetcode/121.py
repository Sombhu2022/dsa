# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
left = 0 #Buy
right = 1 #Sell
max_profit = 0
prices = [7,1,5,3,6,4]

while right < len(prices):
    currentProfit = prices[right] - prices[left] #our current Profit
    if prices[left] < prices[right]:
        max_profit =max(currentProfit,max_profit)
    else:
        left = right
    right += 1
print(max_profit)
            