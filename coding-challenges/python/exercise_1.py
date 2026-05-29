# Step 1: Define the Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Implement the In-Place Reversal
def reverse_list(head: Node) -> Node:
    prev = None       # Tracks the reversed portion
    curr = head       # Current node being processed
    
    while curr:
        # Save the next node before breaking the link
        next_node = curr.next 
        
        # Reverse the current node's pointer
        curr.next = prev 
        
        # Move pointers one step forward
        prev = curr 
        curr = next_node 
        
    # prev is now the new head of the reversed list
    return prev

# Step 3: Helper function to print the list
def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("NULL")

# --- Step 4: Input Data Setup (1 -> 2 -> 3 -> 4 -> 5 -> NULL) ---
# Creating the nodes
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:")
print_list(head)

# Execute the reversal
new_head = reverse_list(head)

print("\nReversed Linked List:")
print_list(new_head)
