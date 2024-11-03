import heapq

def k_smallest_elements(n, A, k):
    # Use a min-heap to find the k smallest elements
    smallest_elements = heapq.nsmallest(k, A)
    
    # Sort the result before returning
    smallest_elements.sort()
    
    return smallest_elements

# Sample Input
n = 10
A = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
k = 3

# Finding the k smallest elements
result = k_smallest_elements(n, A, k)

# Printing the result
print(" ".join(map(str, result)))  # Expected Output: -9 -6 4
