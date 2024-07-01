def fibonacci(n):
    assert int(n) >= 0 and int(n) == n, 'Fibonacci number cannot be negative or non-integer.'
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Fibonacci of which number?: '))
print(fibonacci(n))