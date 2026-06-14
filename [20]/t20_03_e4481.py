import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    tree = [0] * (2 * n)
    
    for i in range(n):
        tree[n + i] = int(input_data[i + 1])
        
    for i in range(n - 1, 0, -1):
        tree[i] = math.gcd(tree[2 * i], tree[2 * i + 1])
        
    m = int(input_data[n + 1])
    idx = n + 2
    out = []
    
    for _ in range(m):
        q = int(input_data[idx])
        if q == 1:
            l = int(input_data[idx + 1]) - 1 + n
            r = int(input_data[idx + 2]) - 1 + n
            res = 0
            while l <= r:
                if l % 2 == 1:
                    res = math.gcd(res, tree[l])
                    l += 1
                if r % 2 == 0:
                    res = math.gcd(res, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            out.append(str(res))
        else:
            pos = int(input_data[idx + 1]) - 1 + n
            val = int(input_data[idx + 2])
            tree[pos] = val
            pos //= 2
            while pos > 0:
                tree[pos] = math.gcd(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2
        idx += 3
        
    print('\n'.join(out))

if __name__ == '__main__':
    main()