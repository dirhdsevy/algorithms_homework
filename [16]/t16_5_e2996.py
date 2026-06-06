import sys

sys.setrecursionlimit(200000)

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    n = int(lines[0].strip())
    root = Node("")
    
    for i in range(1, n + 1):
        if i < len(lines):
            path = lines[i].strip().split('\\')
            curr = root
            for part in path:
                if part not in curr.children:
                    curr.children[part] = Node(part)
                curr = curr.children[part]
                
    def print_tree(node, depth):
        keys = sorted(node.children.keys())
        for k in keys:
            print(" " * depth + k)
            print_tree(node.children[k], depth + 1)
            
    print_tree(root, 0)

if __name__ == '__main__':
    main()