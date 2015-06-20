import datetime, re

infile = open("euler_progress.html", "r")

l = []

for line in infile:
    if "Completed" in line:
        s = line
        for i in xrange(481):
            l.append(s[s.find("Problem %d" % (i+1)):s.find("problem=%d" % (i+2))])
        l.append(s[s.find("Problem 482"):s.find("Problem Solving Awards")])
        #Have now got a list where Problem i is in l[i-1]

completed_list = [i for i in l if "Completed" in i]

second_completed_list = []
for i in completed_list:
    x = i.find("Completed")
    y = i.find("quot")
    second_completed_list.append((i[:i.find(')')+1], i[x:i[x:].find('<') + x], i[y:i[y+1:].find("quot") + y]))

third_completed_list = []
for i in second_completed_list:
    problem_number = int(i[0][i[0].find('m')+2:i[0].find('(')-1]) #Done
    solved_by = int(i[0][i[0].find('by')+3:i[0].find('members')-1])
    completed_date = i[1].split()
    year = int(completed_date[-2][:-1])
    month = "JanFebMarAprMayJunJulAugSepOctNovDec".find(completed_date[-3])/3 +1
    day = int(completed_date[3])
    hour = int(completed_date[-1][:completed_date[-1].find(':')])
    minute = int(completed_date[-1][completed_date[-1].find(':')+1:])
    date_completed = datetime.datetime(year, month, day, hour, minute)
    problem_title = i[2][5:-4] #Done
    third_completed_list.append((problem_number, solved_by, date_completed, problem_title))

sorted_list = sorted(third_completed_list, key = lambda x:x[2])
max_string_length = 0
for i in sorted_list:
    max_string_length = max(max_string_length, len(i[-1]))


def make_table(l):
    for i in l:
        date_solved = str(i[2].date())
        time_solved = str(i[2].time())[:-3]
        title_string = i[-1] + " "*(max_string_length-len(i[-1]))
        print "Problem %3d: %s Solved on %s %s" %(i[0], title_string, date_solved, time_solved)

def make_plot(l):
    pass

make_table(sorted_list)
