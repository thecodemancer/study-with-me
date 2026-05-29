class Node:
    """Standard Node structure for a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head: Node) -> bool:
    """
    Optimal Approach: Floyd's Cycle Detection (Tortoise and Hare)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return False
        
    # Initialize slow and fast pointers at the head
    slow = head
    fast = head
    
    # Fast moves 2 steps while slow moves 1 step
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If pointers meet, there is a cycle
        if slow == fast:
            return True
            
    # If fast reaches the end (None), no cycle exists
    return False

# --- INPUT DATA SETUP ---

# Case 1: Linear List (No Cycle) -> 1 -> 2 -> 3 -> NULL
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

# Case 2: Cyclic List (Cycle exists) -> 1 -> 2 -> 3 -> 2 (back to 2)
head2 = Node(1)
node2 = Node(2)
node3 = Node(3)

head2.next = node2
node2.next = node3
node3.next = node2 # This line creates the cycle by pointing back to an earlier node

# --- TEST EXECUTION ---
print(f"List 1 (Linear) has cycle: {has_cycle(head1)}") # Expected: False
print(f"List 2 (Cyclic) has cycle: {has_cycle(head2)}") # Expected: True
