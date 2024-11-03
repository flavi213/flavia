import random

def partition(A, low, high, pivot_index):
    pivot_value = A[pivot_index]
    # Move pivot to end
    A[pivot_index], A[high] = A[high], A[pivot_index]
    store_index = low
    
    for i in range(low, high):
        if A[i] < pivot_value:
            A[store_index], A[i] = A[i], A[store_index]
            store_index += 1
    
    # Move pivot to its final place
    A[store_index], A[high] = A[high], A[store_index]
    return store_index

def quickselect(A, low, high, k):
    if low == high:  # If the list contains only one element
        return A[low]

    pivot_index = random.randint(low, high)
    pivot_index = partition(A, low, high, pivot_index)

    # The pivot is in its final sorted position
    if k == pivot_index:
        return A[k]
    elif k < pivot_index:
        return quickselect(A, low, pivot_index - 1, k)
    else:
        return quickselect(A, pivot_index + 1, high, k)

def find_kth_smallest(n, A, k):
    return quickselect(A, 0, n - 1, k - 1)  # Convert to 0-based index

# Sample Input
n = 11
A = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
k = 8

# Finding the k-th smallest element
result = find_kth_smallest(n, A, k)

# Printing the result
print(result)  # Expected Output: 13
