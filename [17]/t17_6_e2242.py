import sys

sys.setrecursionlimit(200000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def pre_order(node):
    if node:
        print(node.val, end="")
        pre_order(node.left)
        pre_order(node.right)

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return


    reversed_levels = []
    for line in reversed(lines):
        line = line.strip()
        if line == '*' or not line:
            continue
        reversed_levels.append(line)

    root = None
    for level in reversed_levels:
        for char in level:
            root = insert(root, char)

    pre_order(root)
    print()

if __name__ == '__main__':
    main()