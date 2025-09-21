import numpy as np

# part 1
n = 0
chaine_car = 'mul('
num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
with open("input.txt") as f:
    for line in f:
        for i in range(len(line)-3):
            if line[i:i+4] == chaine_car:
                lengh_num_1 = 0
                while line[i+4+lengh_num_1] in num_set:
                    lengh_num_1 += 1
                if line[i+4+lengh_num_1] == ',':
                    lengh_num_2 = 0
                    while line[i+5+lengh_num_1+lengh_num_2] in num_set:
                        lengh_num_2 += 1
                    if line[i+5+lengh_num_1+lengh_num_2] == ')':
                        n += int(line[i+4:i+4+lengh_num_1]) * int(line[i+5+lengh_num_1:i+5+lengh_num_1+lengh_num_2])

print(n) #result 170068701

# part 2


n = 0
chaine_car_mul = "mul("
chaine_car_dont = "don't()"
chaine_car_do = "do()"
num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
init_bool = True
with open("input.txt") as f:
    for line in f:
        for i in range(len(line)-7):
            if line[i:i+7] == chaine_car_dont:
                init_bool = False
            if line[i:i+4] == chaine_car_do:
                init_bool = True
            if line[i:i+4] == chaine_car_mul:
                lengh_num_1 = 0
                while line[i+4+lengh_num_1] in num_set:
                    lengh_num_1 += 1
                if line[i+4+lengh_num_1] == ',':
                    lengh_num_2 = 0
                    while line[i+5+lengh_num_1+lengh_num_2] in num_set:
                        lengh_num_2 += 1
                    if line[i+5+lengh_num_1+lengh_num_2] == ')':
                        if init_bool:
                            n += int(line[i+4:i+4+lengh_num_1]) * int(line[i+5+lengh_num_1:i+5+lengh_num_1+lengh_num_2])

print(n) #result 78683433

