import sys

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    arr = []
    idx = 1
    
    for _ in range(n):
        if idx + 1 < len(input_data):
            arr.append((int(input_data[idx]), int(input_data[idx+1])))
            idx += 2
            
    merge_sort(arr)
    
    for item in arr:
        print(f"{item[0]} {item[1]}")

if __name__ == '__main__':
    main()