def find_max_subarray_sum(nums):
    """
    Optimal Approach: Kadane's Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle edge case: empty list
    if not nums:
        return 0

    # Initialize tracking variables with the first element
    # current_max: the maximum sum ending at the current position
    # global_max: the overall maximum sum found so far
    current_max = global_max = nums[0]

    # Iterate through the array starting from the second element
    for x in nums[1:]:
        # Decision: Is it better to extend the existing subarray or start fresh?
        # If (current_max + x) is less than x itself, x is better off starting new.
        current_max = max(x, current_max + x)
        
        # Update the global maximum if the new current_max is higher
        if current_max > global_max:
            global_max = current_max

    return global_max

# --- INPUT DATA SETUP ---

# Standard mixed list with positive and negative integers
test_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Case with all negative numbers
negative_nums = [-5, -1, -8, -3]

# --- EXECUTION ---

print(f"Input Array: {test_nums}")
result = find_max_subarray_sum(test_nums)
print(f"The maximum subarray sum is: {result}") 
# Explanation: The subarray [4, -1, 2, 1] gives the maximum sum of 6.

print(f"\nInput Array (All Negatives): {negative_nums}")
result_neg = find_max_subarray_sum(negative_nums)
print(f"The maximum subarray sum is: {result_neg}")
# Explanation: The 'subarray' is just the largest single element, -1.
