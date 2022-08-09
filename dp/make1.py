
input_int = int(input())

min_calc = [0] * (input_int + 6)
divide = [5, 3, 2]
min_calc[1] = 0
min_calc[2] = 1
min_calc[3] = 1
min_calc[5] = 1

def calcmin(num):

    to_divide = []

    if min_calc[num] != 0:
        return min_calc[num]
    else: 
        for i in divide:
            if num % i == 0:
                to_divide.append(i)

        divided = [calcmin(int(num / j)) for j in to_divide] if to_divide else []
        divided.append(calcmin(num-1))
        calc = 1 + min(divided)
        min_calc[num] = calc
        return calc


print(calcmin(input_int))
print(min_calc)

    
    
    