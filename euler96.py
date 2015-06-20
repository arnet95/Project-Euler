#Euler 96

#Sum of three-digit numbers
useful_list = range(1,10)
s = 0

with open("p096_sudoku.txt", "r") as infile:
    for line in infile:
        if line[0] == "G":
            sudoku = []
        else:
            sudoku.append([int(k) for k in line[:-1]])
        if len(sudoku) == 9:
            #Create list_sudoku
            list_sudoku = []
            for i in xrange(9):
                list_sudoku.append([])
                for j in xrange(9):
                    x = sudoku[i][j]
                    if x == 0:
                        list_sudoku[i].append(useful_list)
                    else:
                        list_sudoku[i].append([x])
            s += 1
            print s



            #Solve sudoku
#print s