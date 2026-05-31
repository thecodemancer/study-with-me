from collections import defaultdict

def group_anagrams(words):
    """
    Optimal Approach: Hash Table with Sorted Keys
    Time Complexity: O(n * k log k) where n is number of words and k is max word length
    Space Complexity: O(n * k) to store the results in a dictionary
    """
    # Create a defaultdict where the default value is an empty list
    # This avoids the "if key in dict" check-and-initialize pattern
    anagram_map = defaultdict(list)

    for word in words:
        # 1. Sort the characters of the word to create a 'fingerprint'
        # sorted(word) returns a list of characters, so we join it back to a string
        sorted_key = "".join(sorted(word))
        
        # 2. Append the original word to the list associated with that sorted key
        anagram_map[sorted_key].append(word)

    # Return only the values (the groups of anagrams) as a list of lists
    return list(anagram_map.values())

# --- INPUT DATA SETUP ---

# Standard list of mixed words
input_words = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "silent"]

# --- EXECUTION ---

print(f"Input word list: {input_words}")
result = group_anagrams(input_words)

print("\nGrouped Anagrams:")
for group in result:
    print(group)
