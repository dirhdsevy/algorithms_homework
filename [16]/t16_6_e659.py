import sys

sys.setrecursionlimit(200000)

class GameNode:
    def __init__(self):
        self.children = []
        self.val = None

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
        
    n = int(lines[0].strip())
    nodes = [GameNode() for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        parts = lines[i - 1].split()
        node_type = parts[0]
        parent_id = int(parts[1])
        
        nodes[parent_id].children.append(nodes[i])
        
        if node_type == 'L':
            nodes[i].val = int(parts[2])
            
    def minimax(node, is_max_turn):
        if not node.children:
            return node.val
            
        if is_max_turn:
            return max(minimax(child, False) for child in node.children)
        else:
            return min(minimax(child, True) for child in node.children)
            
    ans = minimax(nodes[1], True)
    
    if ans == 1:
        print("+1")
    else:
        print(ans)

if __name__ == '__main__':
    main()