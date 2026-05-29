def two_sum(nums, target):
    """
    Optimal Approach: Hash Table Lookup
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Dictionary to store the value of the element and its index
    num_map = {}
    
    for i, num in enumerate(nums):
        # Calculate the required value (complement) to reach the target
        complement = target - num
        
        # Check if the complement exists in our dictionary
        if complement in num_map:
            # If found, return the stored index and the current index
            return [num_map[complement], i]
        
        # If not found, store the current number and its index for future steps
        num_map[num] = i
        
    return None

# --- INPUT DATA SETUP ---
# Example 1: Standard input
nums1 = [1, 3, 5, 7, 9, 11]
target1 = 14

# Example 2: Unsorted list with negatives
nums2 = [3, -1, 4, 10]
target2 = 9

# --- TEST EXECUTION ---

# Test Case 1
result1 = two_sum(nums1, target1)
print(f"Test Case 1: nums = {nums1}, target = {target1}")
print(f"Result Indices: {result1} because {nums1[result1[0]]} + {nums1[result1[1]]} equals {target1}") 
# Result Indices: [2, 4] because 5 + 9 equals 14

# Test Case 2
result2 = two_sum(nums2, target2)
print(f"\nTest Case 2: nums = {nums2}, target = {target2}")
print(f"Result Indices: {result2} because {nums2[result2[0]]} + {nums2[result2[1]]} equals {target2}") 
# Result Indices: [1, 3] because -1 + 10 equals 9
