import numpy as np

def test(l):
    return (all(x>0 for x in l) or all(x<0 for x in l)) and (max(l)<4 and min(l)>-4)

# part 1
n=0
with open("input.txt") as f:
    for line in f:
        list= [int(line.split()[i+1])-int(line.split()[i]) for i in range(len(line.split())-1)]
        n += test(list)


print(n) #result 282

# part 2
def test(line):
    list= [int(line[i+1])-int(line[i]) for i in range(len(line)-1)]
    return (all(x>0 for x in list) or all(x<0 for x in list)) and (max(list)<4 and min(list)>-4)

n=0
with open("input.txt") as f:
    for line in f:
        n += any(test(x) for x in [line.split()[:i]+line.split()[i+1:] for i in range(len(line.split()))])

print(n) #result 
