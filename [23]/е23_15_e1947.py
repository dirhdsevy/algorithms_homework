import sys

sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        rev_adj[v].append(u)
        edges.append((u, v))
        idx += 2
        
    visited = [False] * (n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
            
    visited = [False] * (n + 1)
    scc = [0] * (n + 1)
    component_id = 0
    
    def dfs2(u, comp):
        visited[u] = True
        scc[u] = comp
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, comp)
                
    for i in reversed(order):
        if not visited[i]:
            component_id += 1
            dfs2(i, component_id)
            
    condensed_edges = set()
    for u, v in edges:
        cu = scc[u]
        cv = scc[v]
        if cu != cv:
            condensed_edges.add((cu, cv))
            
    print(len(condensed_edges))

if __name__ == '__main__':
    solve()