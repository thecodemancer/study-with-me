from collections import deque

def generate_binary_numbers(n):
    if n <= 0:
        return []

    result = []
    
    # Initialize the queue with the first binary number
    # Using deque ensures O(1) removals from the front
    queue = deque(["1"])

    for _ in range(n):
        # 1. Take the oldest "parent" out of the queue (FIFO)
        current = queue.popleft()
        
        # 2. Add it to our final list
        result.append(current)

        # 3. Generate its children by appending '0' and '1'
        # 4. Add children to the back of the queue to wait their turn
        queue.append(current + "0")
        queue.append(current + "1")

    return result

# Example Execution
n_value = 10
print(f"Binary numbers from 1 to {n_value}:")
print(generate_binary_numbers(n_value))