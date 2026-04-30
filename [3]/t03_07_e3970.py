import sys
from bisect import bisect_left, bisect_right

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    creatures = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    queries = [int(x) for x in input_data[n+2:n+2+m]]
    
    for q in queries:
        count = bisect_right(creatures, q) - bisect_left(creatures, q)
        print(count)