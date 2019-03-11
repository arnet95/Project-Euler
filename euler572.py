list_of_divisors = []
#for i in xrange(40001):


#def all_divisors(n):


def C(n, rank):
    if rank == 0 or rank == 3:
        return 1
    if rank == 1:
        count = 0
        for a in xrange(-200, 201):
            for e in xrange(-200, 201):
                i = 1 - (a+e) #trace(A) = rank(A)

                if abs(i) <= 200:
                    if a*e == 0:

                    else:

                    #Treat a*e = 0 as a special case
                    #for d in all_divisors(a*e):
                    #    b = (a*e)//d
                    #    if abs(b) <= 200:
                    #        count += 1
        return count

print C(200, 1)


def C(n):
    return sum(C(n, i) for i in [0,1,2,3])
