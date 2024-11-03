def insertion_sort_with_swap_count(arr):
    swap_count = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1  # A swap is effectively made here

        arr[j + 1] = key

    return swap_count
    

# Sample Input
n = 6
arr = [6, 10, 4, 5, 1, 2]

# Solve the problem
swaps = insertion_sort_with_swap_count(arr)
swaps
print(swaps)

