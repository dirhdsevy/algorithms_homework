import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def push_back(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop_front(self):
        if self.head is None:
            return "error"
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._size -= 1
        return val

    def pop_back(self):
        if self.tail is None:
            return "error"
        val = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self._size -= 1
        return val

    def front(self):
        if self.head is None:
            return "error"
        return self.head.value

    def back(self):
        if self.tail is None:
            return "error"
        return self.tail.value

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

def solve():
    dq = Deque()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        cmd = parts[0]
        
        if cmd == "push_front":
            dq.push_front(int(parts[1]))
            print("ok")
        elif cmd == "push_back":
            dq.push_back(int(parts[1]))
            print("ok")
        elif cmd == "pop_front":
            print(dq.pop_front())
        elif cmd == "pop_back":
            print(dq.pop_back())
        elif cmd == "front":
            print(dq.front())
        elif cmd == "back":
            print(dq.back())
        elif cmd == "size":
            print(dq.size())
        elif cmd == "clear":
            dq.clear()
            print("ok")
        elif cmd == "exit":
            print("bye")
            break

if __name__ == '__main__':
    solve()