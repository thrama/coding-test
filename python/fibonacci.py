n = int(input("Quanti numeri di Fibonacci vuoi stampare? "))

n_fib = 0
n_fib_next = 1

for i in range(n):
    x = n_fib_next
    n_fib_next += n_fib
    n_fib = x

    print(n_fib)
