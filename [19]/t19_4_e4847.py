import sys

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.pos_map = {}

    def push(self, value, priority):
        if value in self.pos_map:
            idx = self.pos_map[value]
            old_p = self.heap[idx][0]
            self.heap[idx] = (priority, value)
            if priority > old_p:
                self._sift_up(idx)
            else:
                self._sift_down(idx)
        else:
            self.heap.append((priority, value))
            self.pos_map[value] = len(self.heap) - 1
            self._sift_up(len(self.heap) - 1)

    def change(self, value, new_priority):
        if value in self.pos_map:
            idx = self.pos_map[value]
            old_p = self.heap[idx][0]
            self.heap[idx] = (new_priority, value)
            if new_priority > old_p:
                self._sift_up(idx)
            else:
                self._sift_down(idx)

    def pop(self):
        if not self.heap:
            return None
        max_item = self.heap[0]
        last_item = self.heap.pop()
        del self.pos_map[max_item[1]]
        if self.heap:
            self.heap[0] = last_item
            self.pos_map[last_item[1]] = 0
            self._sift_down(0)
        return max_item

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][0] > self.heap[parent][0]:
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            if largest != idx:
                self._swap(idx, largest)
                idx = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos_map[self.heap[i][1]] = i
        self.pos_map[self.heap[j][1]] = j

def main():
    lines = sys.stdin.read().splitlines()
    pq = MaxHeap()
    out = []
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
        
        cmd = parts[0]
        if cmd == "ADD":
            v = parts[1]
            p = int(parts[2])
            pq.push(v, p)
        elif cmd == "CHANGE":
            v = parts[1]
            p = int(parts[2])
            pq.change(v, p)
        elif cmd == "POP":
            item = pq.pop()
            if item:
                out.append(f"{item[1]} {item[0]}")
                
    if out:
        print("\n".join(out))

if __name__ == '__main__':
    main()