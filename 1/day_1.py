import numpy as np

with open("input.txt") as f:
    tab = np.sort(np.array([line.split() for line in f], int).T, axis=1)

print(np.sum(np.abs(tab[0]-tab[1])))
