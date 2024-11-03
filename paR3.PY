def careful_partition(n, A):
    pivot = A[0]  # The first element as the pivot
    less = []
    equal = []
    greater = []

    # Partitioning the array into three categories
    for value in A:
        if value < pivot:
            less.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)
    
    # Create the final partitioned array
    B = less + equal + greater
    return B

# Sample Input
n = 9
A = [4, 5, 6, 4, 1, 2, 5, 7, 4]

# Partitioning the array
result = careful_partition(n, A)

# Printing the result
print(" ".join(map(str, result)))  # Should output something like: 2 1 4 4 4 5 5 6 7
