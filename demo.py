def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n_terms = 10  # Number of terms
fibonacci_series = [fibonacci(i) for i in range(n_terms)]
print(fibonacci_series)

# Fibonacci code explanation 

# This Python code generates the Fibonacci series using a recursive function.
# 
# 1. Function Definition: The `fibonacci(n)` function takes an integer `n` as input.
# 2. Base Cases:
#    - If `n` is less than or equal to 0, it returns 0.
#    - If `n` is 1, it returns 1.
# 3. Recursive Case: For `n` greater than 1, it returns the sum of the two preceding Fibonacci numbers by calling itself with `n-1` and `n-2`.
# 4. Example Usage:
#    - It sets `n_terms` to 10 to generate the first 10 Fibonacci numbers.
#    - It creates a list `fibonacci_series` by calling the `fibonacci` function for values from 0 to 9.
#    - Finally, it prints the Fibonacci series.