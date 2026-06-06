import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop(self):
        if self.head is None:
            return "error"
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return val

    def front(self):
        if self.head is None:
            return "error"
        return self.head.value

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

def solve():
    q = Queue()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        cmd = parts[0]
        
        if cmd == "push":
            q.push(int(parts[1]))
            print("ok")
        elif cmd == "pop":
            print(q.pop())
        elif cmd == "front":
            print(q.front())
        elif cmd == "size":
            print(q.size())
        elif cmd == "clear":
            q.clear()
            print("ok")
        elif cmd == "exit":
            print("bye")
            break

if __name__ == '__main__':
    solve()