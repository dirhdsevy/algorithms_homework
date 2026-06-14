import sys

sys.set_int_max_str_digits(0)

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        a = int(input_data[0])
        b = int(input_data[1])
        
        print(a * b)

if __name__ == '__main__':
    solve()