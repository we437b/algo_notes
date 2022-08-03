# get an int, multiply or add all digits from left -> right

import sys

number = sys.argv[1]

cur = None
add = [0, 1]

for i in number:
    curint = int(i)
    
    if cur == None:
        cur = curint
        continue
    
    if cur in add or i in add:
        cur += curint
        print("adding " + i + " now " + str(cur))
    else:
        cur *= curint
        print("adding " + i + " now " + str(cur))
    
    