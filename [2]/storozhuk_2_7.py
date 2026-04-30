import math

def f(n):
    return 3 * n**2 - n + 4

def g(n):
    return n * math.log(n) + 5

lst = [10, 100, 1000]
print(f"{'n':<10} | {'Sum'}")
for n in lst:
    res = f(n) + g(n)
    print(f"{n:<10} | {res:.2f}")