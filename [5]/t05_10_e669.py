import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    vmax = int(input_data[0])
    d = int(input_data[1])
    N = int(input_data[2])
    
    if N == 0:
        print("00:00")
        return
    
    X = [0] * (N + 1)
    T = [0] * (N + 1)
    
    idx = 3
    for i in range(1, N + 1):
        X[i] = int(input_data[idx])
        hh, mm = map(int, input_data[idx+1].split(':'))
        T[i] = hh * 60 + mm
        idx += 2
        
    x_N = X[N]
    
    A0 = 2 * x_N + N * d * vmax
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        A[i] = T[i] * vmax + 2 * x_N - X[i] + N * d * vmax
        
    f = A[:]
    min_f_N = f[N]
    new_f = [0] * (N + 1)
    
    for m in range(2, N + 1):
        min_prev = f[m-1]
        sub = (m - 1) * d * vmax
        for i in range(m, N + 1):
            val = A[i] - sub
            new_f[i] = val if val > min_prev else min_prev
            if f[i] < min_prev:
                min_prev = f[i]
        
        f, new_f = new_f, f
        if f[N] < min_f_N:
            min_f_N = f[N]
            
    ans_V = A0 if A0 > min_f_N else min_f_N
    ans_mins = (ans_V + vmax - 1) // vmax
    
    hh = (ans_mins // 60) % 24
    mm = ans_mins % 60
    print(f"{hh:02d}:{mm:02d}")

if __name__ == "__main__":
    solve()