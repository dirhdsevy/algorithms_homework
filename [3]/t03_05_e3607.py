import sys

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    it = get_ints()
    
    try:
        while True:
            n = next(it)
            
            counts = [0] * 301
            for _ in range(n):
                h = next(it)
                if 0 <= h <= 300:
                    counts[h] += 1
            
            pref = [0] * 302
            for i in range(301):
                pref[i+1] = pref[i] + counts[i]
            
            a = next(it)
            b = next(it)
            
            l_idx = max(0, a)
            r_idx = min(300, b)
            
            if l_idx > r_idx:
                sys.stdout.write("0\n")
            else:
                sys.stdout.write(str(pref[r_idx+1] - pref[l_idx]) + "\n")
                
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()