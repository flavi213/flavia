import random

def partition(A, low, high):
    pivot_index = random.randint(low, high)
    pivot_value = A[pivot_index]
    # Move pivot to the end
    A[pivot_index], A[high] = A[high], A[pivot_index]
    store_index = low

    for i in range(low, high):
        if A[i] < pivot_value:
            A[store_index], A[i] = A[i], A[store_index]
            store_index += 1
            
    # Move pivot to its final place
    A[store_index], A[high] = A[high], A[store_index]
    return store_index

def quicksort(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)
        quicksort(A, low, pivot_index - 1)
        quicksort(A, pivot_index + 1, high)

def sort_array(n, A):
    quicksort(A, 0, n - 1)
    return A

# Sample Input
n = 7
A = [5, -2, 4, 7, 8, -10, 11]

# Sorting the array
sorted_array = sort_array(n, A)

# Printing the result
print(" ".join(map(str, sorted_array)))  # Expected Output: -10 -2 4 5 7 8 11
