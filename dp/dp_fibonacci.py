# Top-down
td = [0] * 1000 #change 100 to max_length + 1 if you want!
td[1] = 1
td[2] = 1

def fibo(num: int):
    if td[num] != 0:
        return td[num]
    else:
        td[num] = fibo(num-2) + fibo(num-1)
        return td[num]

print(fibo(999))