import sys
import itertools

pos_char = sys.argv[1]

pos_r = int(pos_char[1]) -1
pos_c = ord(pos_char[0]) - 97

max_ind = 8

move = list(filter(lambda c: abs(c[0]) != abs(c[1]), list(itertools.permutations([1, -1, 2, -2], 2))))
counter = 0

for i in move:
    new_pos_r = pos_r + i[0]
    new_pos_c = pos_r + i[1]
    if (0 <= new_pos_r < max_ind) and (0 <= new_pos_c < max_ind):
        counter += 1

print(counter)