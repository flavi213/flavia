def merge_sorted_arrays(A, B):
    # Initialize pointers for both arrays
    i, j = 0, 0
    C = []
    
    # Merge arrays by comparing elements at each pointer
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    # Append remaining elements from A or B if any
    C.extend(A[i:])
    C.extend(B[j:])
    
    return C

# Example usage
n = 4
A = [2, 4, 10, 18]
m = 3
B = [-5, 11, 12]
print(merge_sorted_arrays(A, B))  # Output should be [-5, 2, 4, 10, 11, 12, 18]