import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_forward(self):
        current = self.head
        res = []
        while current is not None:
            res.append(str(current.value))
            current = current.next
        if res:
            print(" ".join(res))

    def print_backward(self):
        def _print_rev(node, is_first=True):
            if node is None:
                return
            _print_rev(node.next, False)
            if is_first:
                print(node.value)
            else:
                print(node.value, end=" ")
        
        if self.head is not None:
            _print_rev(self.head)

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    lst = LinkedList()
    
    line_idx = 0
    while line_idx < len(lines) and not lines[line_idx].strip():
        line_idx += 1
        
    if line_idx >= len(lines):
        return
        
    line_idx += 1
    elements_found = False
    
    while line_idx < len(lines):
        curr_line = lines[line_idx].strip()
        if curr_line:
            for val in curr_line.split():
                lst.append(int(val))
            elements_found = True
            break
        line_idx += 1

    if elements_found:
        lst.print_forward()
        lst.print_backward()

if __name__ == '__main__':
    main()