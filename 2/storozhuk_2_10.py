def f1(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def f2(n):
    return n * (n + 1) // 2

n = 100
print(f1(n))
print(f2(n))