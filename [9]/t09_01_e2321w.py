import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    arr.sort()
    print(*(arr))

if __name__ == "__main__":
    solve()