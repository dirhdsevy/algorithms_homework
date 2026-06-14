import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    p = int(input_data[2])

    idx = 3
    dangerous = set()
    for _ in range(p):
        dangerous.add(int(input_data[idx]))
        idx += 1

    edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((w, u, v))
        idx += 3

    if n == 1:
        print(0)
        return

    if p == n:
        if n == 2:
            min_w = float('inf')
            for w, u, v in edges:
                if (u == 1 and v == 2) or (u == 2 and v == 1):
                    min_w = min(min_w, w)
            if min_w == float('inf'):
                print("impossible")
            else:
                print(min_w)
        else:
            print("impossible")
        return

    safe_nodes = set(range(1, n + 1)) - dangerous

    parent = {x: x for x in safe_nodes}
    
    def find(i):
        while i != parent[i]:
            parent[i] = parent[parent[i]] 
            i = parent[i]
        return i

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    safe_edges = []
    for w, u, v in edges:
        if u in safe_nodes and v in safe_nodes:
            safe_edges.append((w, u, v))

    safe_edges.sort()

    mst_cost = 0
    edges_used = 0

    for w, u, v in safe_edges:
        if union(u, v):
            mst_cost += w
            edges_used += 1

    if edges_used != len(safe_nodes) - 1:
        print("impossible")
        return

    total_cost = mst_cost
    min_to_safe = {d: float('inf') for d in dangerous}
    
    for w, u, v in edges:
        if u in dangerous and v in safe_nodes:
            min_to_safe[u] = min(min_to_safe[u], w)
        elif v in dangerous and u in safe_nodes:
            min_to_safe[v] = min(min_to_safe[v], w)
            
    for d in dangerous:
        if min_to_safe[d] == float('inf'):
            print("impossible")
            return
        total_cost += min_to_safe[d]

    print(total_cost)

if __name__ == '__main__':
    solve()