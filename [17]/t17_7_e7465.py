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
    else:
        root.right = insert(root.right, val)
    return root

def is_same(r1, r2):
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False
    return r1.val == r2.val and is_same(r1.left, r2.left) and is_same(r1.right, r2.right)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr1 = [int(x) for x in input_data[1:n+1]]
    
    m = int(input_data[n+1])
    arr2 = [int(x) for x in input_data[n+2:n+2+m]]

    root1 = None
    for val in arr1:
        root1 = insert(root1, val)

    root2 = None
    for val in arr2:
        root2 = insert(root2, val)

    if is_same(root1, root2):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()