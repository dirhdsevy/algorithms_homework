import sys
import random

sys.setrecursionlimit(20000)

def quick_sort(arr, left, right):
    if left >= right:
        return
    
    pivot = arr[random.randint(left, right)]
    i, j = left, right
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    quick_sort(arr, left, j)
    quick_sort(arr, i, right)

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) > 1:
        arr = [int(x) for x in input_data[1:]]
        quick_sort(arr, 0, len(arr) - 1)
        print(*(arr))

if __name__ == '__main__':
    main()