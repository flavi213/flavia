def heapify(A, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and A[left] > A[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and A[right] > A[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Swap
        heapify(A, n, largest)  # Recursively heapify the affected subtree

def build_max_heap(A):
    n = len(A)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

# Sample Input
n = 5
A = [1, 3, 5, 7, 2]

# Building the max heap
build_max_heap(A)

# Printing the result
print(" ".join(map(str, A)))  # Expected Output: 7 5 1 3 2
