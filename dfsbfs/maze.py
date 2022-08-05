import sys
from collections import deque

n = int(sys.argv[1])
m = int(sys.argv[2])
maze_char = sys.argv[3:]

visited = []

maze = [[int(i) for i in j] for j in maze_char]

q = deque([(0,0)])
visited.append((0,0))
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    r,c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < n and nc >= 0 and nc < m:
            if maze[nr][nc] != 0 and (nr, nc) not in visited:
                q.append((nr, nc))
                visited.append((nr, nc))
                maze[nr][nc] = maze[r][c] + 1

print(maze)

print(maze[n-1][m-1])