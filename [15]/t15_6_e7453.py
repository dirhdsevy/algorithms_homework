import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def size(self):
        return self._size

    def rotate(self, k):
        if self.head is None or self.head.next is None or k == 0:
            return

        k = k % self._size
        if k == 0:
            return

        self.tail.next = self.head

        steps_to_new_tail = self._size - k
        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        self.tail = new_tail
        self.tail.next = None

    def print_list(self):
        current = self.head
        res = []
        while current is not None:
            res.append(str(current.value))
            current = current.next
        if res:
            print(" ".join(res))

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    clean_lines = []
    for line in lines:
        line_stripped = line.strip()
        if line_stripped:
            clean_lines.append(line_stripped)

    if len(clean_lines) < 3:
        return

    n = int(clean_lines[0])
    
    lst = LinkedList()
    for val in clean_lines[1].split():
        lst.append(int(val))
        
    k = int(clean_lines[2])

    lst.rotate(k)
    lst.print_list()

if __name__ == '__main__':
    main()