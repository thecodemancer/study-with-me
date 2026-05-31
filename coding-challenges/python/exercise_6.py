def merge_dictionaries_new(dict1, dict2):
    """
    Creates a new dictionary using unpacking.
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    # The ** operator unpacks the dictionaries. 
    # If keys collide, the rightmost (dict2) takes precedence.
    merged = {**dict1, **dict2}
    return merged

def merge_dictionaries_inplace(dict1, dict2):
    """
    Updates the first dictionary in-place.
    Time Complexity: O(m) where m is size of dict2
    Space Complexity: O(1) extra space
    """
    dict1.update(dict2)
    return dict1

# --- INPUT DATA SETUP ---

# Original user profile
base_profile = {
    "username": "coder_99",
    "email": "old_email@example.com",
    "level": 5,
    "theme": "light"
}

# Updates to be applied (note the email and theme collisions)
profile_update = {
    "email": "new_dev_email@pro.com",
    "theme": "dark",
    "location": "San Francisco"
}

# --- EXECUTION ---

print("--- Method 1: Dictionary Unpacking (New Object) ---")
# Preserving base_profile by creating a new dictionary
new_profile = merge_dictionaries_new(base_profile, profile_update)

print(f"Original remains unchanged: {base_profile['email']}")
print(f"New Merged Profile: {new_profile}")
# Result: email is updated to 'new_dev_email@pro.com' and theme is 'dark'


print("\n--- Method 2: .update() (In-Place Mutation) ---")
# This will modify the base_profile dictionary directly
merge_dictionaries_inplace(base_profile, profile_update)

print(f"Original has been mutated: {base_profile['email']}")
print(f"Updated Original: {base_profile}")
