def fibonacci(n):
    a, b = 0, 1
    i=0
    while i<n:
        yield a
        a, b = b, a + b
        i+=1

def print_fib(n):
    for num in fibonacci(n):
        print(num, end=" ")

print_fib(5)