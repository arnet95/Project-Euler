#Euler185

with open('euler185.txt', 'r')  as infile:
    d = {}
    for line in infile:
        x = int(line.split(';')[1][:1])
        y = line[:line.find(';')]
        if x == 0:
            s = y
        d[y] = x



possible_solutions = {}
for i in xrange(16):
    l = []
    for key in d:
        l.append(int(key[i]))
    possible_solutions[i] = list(set(l))
    possible_solutions[i].remove(int(s[i]))
    

print possible_solutions