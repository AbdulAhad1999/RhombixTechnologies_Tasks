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
