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
nums1 = [1, 2, 3, 4, 5, 6, 7]
target1 = 9

# Example 2: Unsorted list with negatives
nums2 = [3, -1, 4, 10]
target2 = 9

# --- TEST EXECUTION ---

# Test Case 1
result1 = two_sum(nums1, target1)
print(f"Test Case 1: nums = {nums1}, target = {target1}")
print(f"Result Indices: {result1} because {nums1[result1[0]]} + {nums1[result1[1]]} equals {target1}") 
# Explanation: nums + nums[5] = 2 + 7 = 9

# Test Case 2
result2 = two_sum(nums2, target2)
print(f"\nTest Case 2: nums = {nums2}, target = {target2}")
print(f"Result Indices: {result2} because {nums2[result2[0]]} + {nums2[result2[1]]} equals {target2}") 
# Explanation: nums[5] + nums[6] = -1 + 10 = 9
