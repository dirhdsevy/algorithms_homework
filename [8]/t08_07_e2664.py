n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    key = arr[i]
    j = i - 1
    moved = False
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        moved = True
    arr[j + 1] = key
    if moved:
        print(*(arr))