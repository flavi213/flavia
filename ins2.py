
def count_insertion_sort_swaps(n, A):
    swaps = 0
    # Start from the second element
    for i in range(1, n):
        key = A[i]
        j = i - 1
        
        # Move elements of A[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            swaps += 1  # Each time we move an element, count it as a swap
            j -= 1
        A[j + 1] = key
        
    return swaps

# Sample Input
n = 6
A = [6, 10, 4, 5, 1, 2]

# Counting swaps
result = count_insertion_sort_swaps(n, A)
print(result)  
