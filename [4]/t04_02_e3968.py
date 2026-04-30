import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    c = float(input_data[0])
    l, r = 0.0, 100000.0
    
    for _ in range(100):
        mid = (l + r) / 2.0
        if mid * mid + math.sqrt(mid) < c:
            l = mid
        else:
            r = mid
            
    print(f"{l:.10f}")

if __name__ == "__main__":
    solve()