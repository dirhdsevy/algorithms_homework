import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    while True:
        try:
            N = int(next(iterator))
            num_tracks = int(next(iterator))
            
            tracks = []
            for _ in range(num_tracks):
                tracks.append(int(next(iterator)))
                
        except StopIteration:
            break  

        dp = [False] * (N + 1)
        dp[0] = True

        for track_len in tracks:
            for w in range(N, track_len - 1, -1):
                if dp[w - track_len]:
                    dp[w] = True

        max_w = N
        while max_w >= 0 and not dp[max_w]:
            max_w -= 1

        print(f"sum:{max_w}")

if __name__ == '__main__':
    solve()