#!/usr/bin/env python3

def fib(x):
    a, b = 0, 1
    while b < x:
        print(b, end=' ', flush = True)
        a, b = b, a + b
fib(10000)

print()

def prime(i):
    if i<=1:
        return False
    for x in range(2, i):
        if i % x == 0:
            return False
    else:
        return True
i = 5
if prime(i):
    print(f"{i} is prime")
else:
    print(f"{i} is not prime")


x = 10
y = 5
print(x**y)