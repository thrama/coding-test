"""
Link: https://en.wikipedia.org/wiki/Fibonacci_number
"""

n = int(input("How mamy Fibonacci's numbers you want to print? "))

n_fib = 0
n_fib_next = 1

for i in range(n):
    n_fib, n_fib_next = n_fib_next, n_fib_next+n_fib

    print(n_fib)
