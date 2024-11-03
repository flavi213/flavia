def rabbit_population(n, k):
    # Initial conditions
    F1, F2 = 1, 1
    
    # Base cases for n = 1 and n = 2
    if n == 1:
        return F1
    elif n == 2:
        return F2
    
    # Dynamic programming approach for n > 2
    for month in range(3, n + 1):
        Fn = F2 + k * F1  # recurrence relation
        F1, F2 = F2, Fn   # move to next terms in sequence
    
    return Fn

result = rabbit_population(35 , 4)
print(result)  # Expected output: 19