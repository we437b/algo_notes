# get two arguments, divide by second argument or subtract 1 until its 1
import sys

target = int(sys.argv[1])
k = int(sys.argv[2])

# counter for number of operations
counter = 0

while target != 1:
    val = target % k
    if val != 0:
        target -= 1
        counter += 1
        print("Subtracting 1.. currently" + str(target))
    else:
        target /= k
        counter += 1
        print("dividing by k.. curently" + str(target))

print(counter)
    