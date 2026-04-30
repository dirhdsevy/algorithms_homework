import sys
from bisect import bisect_left

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    collection = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    queries = [int(x) for x in input_data[n+2:n+2+m]]
    
    for q in queries:
        pos = bisect_left(collection, q)
        if pos < n and collection[pos] == q:
            print("YES")
        else:
            print("NO")