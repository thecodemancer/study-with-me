def find_second_largest(numbers):
    # Handle edge case: list must have at least two elements
    if len(numbers) < 2:
        return "List must contain at least two distinct numbers."

    # Initialize tracking variables to negative infinity
    # This ensures the logic works even with negative integers
    largest = float('-inf')
    second_largest = float('-inf')

    for x in numbers:
        # If the current number is greater than the largest found so far
        if x > largest:
            # The old largest becomes the second largest
            second_largest = largest
            # Update the absolute largest
            largest = x
        
        # If the number is between the largest and second largest
        elif x > second_largest and x != largest:
            second_largest = x

    # Final check to see if a second largest was actually found
    if second_largest == float('-inf'):
        return "There is no unique second largest element."
    
    return second_largest

# --- INPUT DATA SETUP ---

# Standard list of integers
test_list = [1, 2, 3, 4, 50]

# Additional test case with negative numbers
negative_list = [-5, -1, -10, -3, -2]

# --- EXECUTION ---

print(f"Input List: {test_list}")
result = find_second_largest(test_list)
print(f"The second largest element is: {result}")

print(f"\nInput List: {negative_list}")
result_neg = find_second_largest(negative_list)
print(f"The second largest element is: {result_neg}")
