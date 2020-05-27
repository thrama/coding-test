n = int(input("Quanti numeri di Fibonacci vuoi stampare? "))

n_fib = 0
n_fib_next = 1

for i in range(n):
    n_fib, n_fib_next = n_fib_next, n_fib_next+n_fib

    print(n_fib)
