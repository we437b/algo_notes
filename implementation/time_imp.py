import sys

time = int(sys.argv[1])

cur_hr = 0
cur_min = 0
cur_sec = 0

counter = 0

while cur_hr <= time:
    if '3' in str(cur_hr):
        counter += 3600
    else:    
        while cur_min <= 59:
            if '3' in str(cur_min):
                counter += 60
            else:
                while cur_sec <= 59:
                    if '3' in (str(cur_sec)):
                        counter += 1
                    cur_sec += 1    
            cur_min += 1
            cur_sec = 0
    cur_hr += 1
    cur_min = 0

print(counter)