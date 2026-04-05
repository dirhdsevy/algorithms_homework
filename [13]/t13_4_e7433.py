import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    a = int(input_data[0])
    p = int(input_data[1])

    if a == 0:
        print(0)
        return

    res = []
    while a > 0:
        rem = a % p
        if rem < 10:
            res.append(str(rem))
        else:
            res.append(f"[{rem}]")
        a //= p

    print("".join(res[::-1]))


if __name__ == "__main__":
    solve()
