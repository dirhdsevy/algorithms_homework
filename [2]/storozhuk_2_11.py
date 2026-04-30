def f(n):
    return n * (n + 1) // 2

def g1(n):
    s = 0
    for i in range(1, n + 1):
        s += i + f(i)
    return s

def g2(n):
    a = (n * (n + 1) * (n + 2)) // 6
    b = (n * (n + 1)) // 2
    return a + b

n = 10
print(g1(n))
print(g2(n))