import numpy as np

# part 1
with open("input.txt") as f:
    tab = np.sort(np.array([line.split() for line in f], int).T, axis=1)

print(np.sum(np.abs(tab[0]-tab[1]))) #result (2580760)

#part 2
temp = 0
for i in tab[0]:
    temp += i * np.sum([j==i for j in tab[1]])

print(temp) #result (25358365)