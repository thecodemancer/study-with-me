# Exercise 1: Reversing a Singly Linked List In-Place
# Step 1: Define the Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    # Step 2: Initialize three pointers
    prev = None
    curr = head
    
    # Step 3: Iterate through the list
    while curr:
        # Step 4: Save the next node so we don't break the chain [2]
        next_node = curr.next
        
        # Step 5: Reverse the current node's pointer
        curr.next = prev
        
        # Step 6: Move prev and curr one step forward
        prev = curr
        curr = next_node
        
    # Step 7: Return prev as the new head of the reversed list
    return prev

# --- Manual Input Data Setup (1 -> 2 -> 3 -> 4 -> 5 -> NULL) ---
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Perform the reversal
new_head = reverse_list(head)

# Optional: Print the result to verify
temp = new_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("NULL")