import sys

sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    start_vertex = int(input_data[1])
    

    edges = []
    idx = 2
    max_v = max(n, start_vertex)
    
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        edges.append((u, v))
        max_v = max(max_v, u, v)
        idx += 2
        
    adj = [[] for _ in range(max_v + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    color = [-1] * (max_v + 1)
    color[start_vertex] = 0
    q = [start_vertex]
    part_left = []
    
    while q:
        u = q.pop(0)
        if color[u] == 0:
            part_left.append(u)
            
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)

    def find_matching(ignore_vertex=-1):
        match = [-1] * (max_v + 1)
        
        def dfs(u, visited):
            for v in adj[u]:
                if v == ignore_vertex:
                    continue
                if not visited[v]:
                    visited[v] = True
                    if match[v] == -1 or dfs(match[v], visited):
                        match[v] = u
                        return True
            return False

        matching_size = 0
        for u in part_left:
            if u == ignore_vertex:
                continue
            visited = [False] * (max_v + 1)
            if dfs(u, visited):
                matching_size += 1
        return matching_size, match

    original_size, _ = find_matching()
    size_without_start, _ = find_matching(ignore_vertex=start_vertex)
    
    if size_without_start < original_size:
        best_moves = []
        for v in adj[start_vertex]:
            def find_matching_ignore_two(ign1, ign2):
                match = [-1] * (max_v + 1)
                def dfs_two(u, visited):
                    for neighbor in adj[u]:
                        if neighbor == ign1 or neighbor == ign2: continue
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            if match[neighbor] == -1 or dfs_two(match[neighbor], visited):
                                match[neighbor] = u
                                return True
                    return False

                m_size = 0
                for u in part_left:
                    if u == ign1 or u == ign2: continue
                    visited = [False] * (max_v + 1)
                    if dfs_two(u, visited):
                        m_size += 1
                return m_size

            size_without_both = find_matching_ignore_two(start_vertex, v)
            
            if size_without_both == original_size - 1:
                 best_moves.append(v)
                 
        if best_moves:
            print(f"First player wins flying to airport {min(best_moves)}")
        else:
            print("First player loses")
    else:
        print("First player loses")

if __name__ == '__main__':
    solve()