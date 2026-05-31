def max_stock_profit(prices):
    """
    Optimal Approach: Single-Pass Greedy Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not prices or len(prices) < 2:
        return 0

    # Initialize min_price to the first day's price
    # Initialize max_profit to 0 (assuming no profit is made yet)
    min_price = prices[0]
    max_profit = 0

    # Start scanning from the second day
    for price in prices[1:]:
        # 1. Update the minimum price seen so far
        if price < min_price:
            min_price = price
        
        # 2. Calculate potential profit if we sold at the current price
        potential_profit = price - min_price
        
        # 3. Update max_profit if this potential profit is a new record
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit

# --- INPUT DATA SETUP ---
# Example: Prices rise, fall, and then spike
daily_prices = [5,6,7,4,9,11,3,5,12]

# --- EXECUTION ---
print(f"Daily Stock Prices: {daily_prices}")
profit = max_stock_profit(daily_prices)
print(f"Maximum achievable profit: {profit}") 
# Explanation: Buy at 3, sell at 12 = Profit of 9.
