import sys
from collections import deque


tray_char = sys.argv[1:]

chunks = 0
visited = []

tray = [[int(i) for i in j] for j in tray_char]


def BFS(tray, starti, startj):
    queue = deque([(starti, startj)])
    visited.append((starti, startj))
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= 0 and nr < len(tray) and nc >= 0 and nc < len(tray[0]):
                if tray[nr][nc] == 0 and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.append((nr, nc))
          
                

temp_chunk = []
for i in range(len(tray_char)):
    for j in range(len(tray_char[0])):
        if (i,j) not in visited and tray[i][j] != 1:
            chunks += 1
            BFS(tray, i, j)

print(chunks)
    