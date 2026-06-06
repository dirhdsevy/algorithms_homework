import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = [0] + [int(x) for x in input_data[1:n+1]]
    
    is_heap = True
    for i in range(1, n // 2 + 1):
        if 2 * i <= n and arr[i] > arr[2 * i]:
            is_heap = False
            break
        if 2 * i + 1 <= n and arr[i] > arr[2 * i + 1]:
            is_heap = False
            break
            
    if is_heap:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()