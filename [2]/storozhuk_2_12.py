def f(n):
    return n * (n + 1) // 2

def g(n):
    a = (n * (n + 1) * (n + 2)) // 6
    b = (n * (n + 1)) // 2
    return a + b

def h(n):
    return f(n) + g(n)

print(h(10))