def fibonacci_basic(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_basic(n - 1) + fibonacci_basic(n - 2)


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = [0] * (n + 1)
    if n == 0 or n == 1:
        return n
    if memo[n] == 0:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_dynamic(n):
    if n == 0:
        return n
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b
