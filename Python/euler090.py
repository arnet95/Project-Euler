#Listing all the numbers which should be on the cubes
numbers = [(0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)]

#Generating all the possible cubes
l = []
for a in xrange(0, 5):
    for b in xrange(a+1, 6):
        for c in xrange(b+1, 7):
            for d in xrange(c+1, 8):
                for e in xrange(d+1, 9):
                    for f in xrange(e+1, 10):
                        l.append((a, b, c, d, e, f))

count = 0
for i in l:
    for j in l:
        #Allowing for reversals of 6 and 9
        if 6 in i or 9 in i:
            i = i + (6, 9)
        if 6 in j or 9 in j:
            j = j + (6, 9)
        #Checking if each number can be found on the cubes
        boolean = True
        for number in numbers:
            digit1, digit2 = number
            if (digit1 in i and digit2 in j) or (digit2 in i and digit1 in j):
                boolean = boolean
            else:
                boolean = False
        if boolean:
            count += 1

#Accounting for double counting
print count // 2
