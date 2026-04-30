import sys

n_str = sys.stdin.read().strip()
if n_str:
    n = int(n_str)
    s = bin(n)[2:]
    max_m = n
    for i in range(len(s)):
        s = s[1:] + s[0]
        max_m = max(max_m, int(s, 2))
    print(max_m)