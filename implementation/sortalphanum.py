import sys

inp = sys.argv[1]

sum = 0
alpha = []

for i in inp:
    if i.isalpha():
        alpha.append(i)
    else:
        sum += int(i) 
    
alpha.sort()

if sum != 0:
    alpha.append(str(sum))

print(''.join(alpha))