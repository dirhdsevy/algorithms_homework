import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    robots = []
    
    for i in range(n):
        main_num = input_data[1 + 2*i]
        aux_num = input_data[2 + 2*i]
        robots.append((int(main_num), aux_num))
    
    robots.sort(key=lambda x: x[0])
    
    output = [f"{r[0]} {r[1]}" for r in robots]
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()