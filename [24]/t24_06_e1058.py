import sys
from collections import deque

WALL_CHAR = "*"
CELL_CHAR = "·"

class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.m = len(maze[0])
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def mark_lake(self, si, sj, num):
        if isinstance(self.maze[si][sj], int):
            return 0

        count = 0
        queue = deque([(si, sj)])
        self.maze[si][sj] = num

        while queue:
            i, j = queue.popleft()
            count += 1

            for di, dj in self.directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < self.n and 0 <= nj < self.m:
                    if not isinstance(self.maze[ni][nj], int) and self.maze[ni][nj] == CELL_CHAR:
                        self.maze[ni][nj] = num
                        queue.append((ni, nj))
        return count

if __name__ == "__main__":
    with open("input.txt") as f:
        N, M, K = map(int, f.readline().split())

        maze_matrix = [[WALL_CHAR] * M for _ in range(N)]
        submerged = []
        
        for _ in range(K):
            i, j = map(lambda x: int(x) - 1, f.readline().split())
            maze_matrix[i][j] = CELL_CHAR
            submerged.append((i, j))

        maze = Maze(maze_matrix)
        max_lake_size = 0
        
        for idx, cell in enumerate(submerged):
            max_lake_size = max(maze.mark_lake(*cell, idx), max_lake_size)
            
        print(max_lake_size)