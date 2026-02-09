import sys
sys.setrecursionlimit(2000)

def task_a(n):
    if n <= 0: return 0
    return task_a(n - 1) + 1

def task_d(n, a):
    if n <= a: return 1
    return a * task_d(n - a, a) + 1

def task_g(n, a):
    if n < a: return 1
    return a * task_g(n // a, a) + 1

def task_h(n, a):
    if n < a: return 1
    return a * task_h(n // a, a) + n

n = 100
a = 2
print(task_a(n))
print(task_d(n, a))
print(task_g(n, a))
print(task_h(n, a))