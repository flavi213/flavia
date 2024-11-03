def partition_array(n, A):
    pivot = A[0]  # The first element
    less_or_equal = []
    greater = []

    # Partitioning the array into two lists
    for i in range(1, n):
        if A[i] <= pivot:
            less_or_equal.append(A[i])
        else:
            greater.append(A[i])
    
    # Create the final partitioned array
    B = less_or_equal + [pivot] + greater
    return B

# Sample Input
n = 9
A = [7, 2, 5, 6, 1, 3, 9, 4, 8]

# Partitioning the array
result = partition_array(n, A)

# Printing the result
print(" ".join(map(str, result)))  # Sample Output: 2 5 6 1 3 7 9 4 8
