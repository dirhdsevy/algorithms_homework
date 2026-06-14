import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        in_degree[v] += 1
        idx += 2
        
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(topo_order) == n:
        print(*(topo_order))
    else:
        print(-1)

if __name__ == '__main__':
    solve()