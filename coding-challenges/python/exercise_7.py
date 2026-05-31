def count_frequencies(items):
    """
    Optimal Approach: Dictionary .get() method
    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(k) - Where k is the number of unique elements
    """
    frequency_map = {}
    
    for item in items:
        # .get(item, 0) returns the current count or 0 if item is new
        # We then add 1 and store it back in the dictionary
        frequency_map[item] = frequency_map.get(item, 0) + 1
        
    return frequency_map

# --- INPUT DATA SETUP ---

# Example 1: List of strings (Words)
word_list = ["apple", "banana", "orange", "apple", "apple", "banana", "grape"]

# Example 2: List of integers (IDs)
id_list = [1,2,3,4]

# --- EXECUTION ---

print("--- Word Frequency Results ---")
word_counts = count_frequencies(word_list)
print(f"Input: {word_list}")
print(f"Counts: {word_counts}")

print("\n--- ID Frequency Results ---")
id_counts = count_frequencies(id_list)
print(f"Input: {id_list}")
print(f"Counts: {id_counts}")
