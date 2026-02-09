def calc_a(n):
    return n * (n + 1) // 2

def calc_b(n):
    return n * (n + 1) * (2 * n + 1) // 6

def calc_c(n, a):
    if a == 1: return n + 1
    return (a**(n + 1) - 1) // (a - 1)

n = 10
a = 2
print(calc_a(n))
print(calc_b(n))
print(calc_c(n, a))