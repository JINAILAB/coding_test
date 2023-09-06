import sys
sys.setrecursionlimit(100000)

def fib(n, memorization={}):
    if n in memorization:
        return memorization[n]

    if n == 1:
        return 1
    if n == 0:
        return 0

    value = fib(n-1, memorization) + fib(n-2, memorization)
    memorization[n] = value
    return value

print(fib(int(input())))