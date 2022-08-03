# always starting from (1,1), A will move in LRUDUD.. etc
# erroneous movement will be ignored

import sys

num = int(sys.argv[1])

plan = sys.argv[2:]

dir = ["D", "U", "R", "L"] 
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

pos_r = 1
pos_c = 1

for i in plan:
    ind = dir.index(i)
    new_pos_r = dr[ind] + pos_r
    new_pos_c = dc[ind] + pos_c
    if new_pos_r > 0 and new_pos_r <= num and new_pos_c > 0 and new_pos_r <= num:
        pos_r = new_pos_r
        pos_c = new_pos_c
    
print(str(pos_r) + " " + str(pos_c))
    
    