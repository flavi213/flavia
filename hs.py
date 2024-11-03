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

def heap_sort(A):
    n = len(A)
    build_max_heap(A)  # Step 1: Build a max heap
    
    # Step 2: One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  # Swap the root (max) with the last element
        heapify(A, i, 0)  # Heapify the root element to maintain the heap property

# Sample Input
n = 9
A = [2, 6, 7, 1, 3, 5, 4, 8, 9]

# Performing heap sort
heap_sort(A)

# Printing the result
print(" ".join(map(str, A)))  # Expected Output: 1 2 3 4 5 6 7 8 9
