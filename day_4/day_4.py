

with open("input.txt") as f:
    tab = [list(line.rstrip('\n')) for line in f]

# part 1
n=0
for i in range(len(tab)):
    for j in range(len(tab[0])):
        if j+3 < len(tab[0]):
            if tab[i][j] == 'X' and tab[i][j+1] == 'M' and tab[i][j+2] == 'A' and tab[i][j+3] == 'S':
                n += 1
        if j-3 >= 0:
            if tab[i][j] == 'X' and tab[i][j-1] == 'M' and tab[i][j-2] == 'A' and tab[i][j-3] == 'S':
                n += 1
        if i+3 < len(tab):
            if tab[i][j] == 'X' and tab[i+1][j] == 'M' and tab[i+2][j] == 'A' and tab[i+3][j] == 'S':
                n += 1
        if i-3 >= 0:
            if tab[i][j] == 'X' and tab[i-1][j] == 'M' and tab[i-2][j] == 'A' and tab[i-3][j] == 'S':
                n += 1
        if i+3 < len(tab) and j+3 < len(tab[0]):
            if tab[i][j] == 'X' and tab[i+1][j+1] == 'M' and tab[i+2][j+2] == 'A' and tab[i+3][j+3] == 'S':
                n += 1
        if i-3 >= 0 and j-3 >= 0:
            if tab[i][j] == 'X' and tab[i-1][j-1] == 'M' and tab[i-2][j-2] == 'A' and tab[i-3][j-3] == 'S':
                n += 1
        if i+3 < len(tab) and j-3 >= 0:
            if tab[i][j] == 'X' and tab[i+1][j-1] == 'M' and tab[i+2][j-2] == 'A' and tab[i+3][j-3] == 'S':
                n += 1
        if i-3 >= 0 and j+3 < len(tab[0]):
            if tab[i][j] == 'X' and tab[i-1][j+1] == 'M' and tab[i-2][j+2] == 'A' and tab[i-3][j+3] == 'S':
                n += 1


print(n) #result 2599


# part 2

n=0

for i in range(1,len(tab)-1):
    for j in range(1,len(tab[0])-1):
        if tab[i][j] == 'A':
            if ((tab[i-1][j-1] == 'M' and tab[i+1][j+1] == 'S') or (tab[i-1][j-1] == 'S' and tab[i+1][j+1] == 'M')) and ((tab[i+1][j-1] == 'M' and tab[i-1][j+1] == 'S') or (tab[i+1][j-1] == 'S' and tab[i-1][j+1] == 'M')):
                n += 1
                
print(n) #result 1948