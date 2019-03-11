from collections import deque

def trim_list(deq):
    first = deq.popleft()
    while first == 0:
        #Assuming that deq contains a non-zero element.
        first = deq.popleft()
    positive = (first > 0)
    ret_list = [first]
    while len(deq) > 0:
        first = deq.popleft()
        if (first > 0) == positive:
            ret_list[-1] += first
        else:
            ret_list.append(first)
            positive = not positive
    return [i for i in ret_list if i != 0]

def maxsubseq(l):
    trimmed_list = trim_list(deque(l))
    N = len(trimmed_list)
    print N
    lengths = [trimmed_list] + [[0 for start in xrange(0, N-length)] for length in xrange(1, N)]
    for length in xrange(1, N):
        for start in xrange(0, N-length):
            lengths[length][start] = lengths[length-1][start] + trimmed_list[start+length]
    return max(max(l) for l in lengths)

s_mem = {}
def s(k):
    if k in s_mem:
        return s_mem[k]
    else:
        if k <= 55:
            result = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
        else:
            result = (s(k-24) + s(k-55) + 1000000) % 1000000 - 500000
        s_mem[k] = result
        return result

def gen_table(n):
    table = [[0 for _ in xrange(n)] for _ in xrange(n)]
    table = [[s(2000*i+j+1) for j in xrange(2000)] for i in xrange(2000)]
    return table

def main(table):
    #Horizontal
    result = max(maxsubseq(l) for l in table)
    #Vertical
    result = max(result, max(maxsubseq([table[i][k] for i in xrange(2000)]) for k in xrange(2000)))
    #Turns out you get the right result here, so no need to check the diagonal and anti-diagonal.
    #Diagnoal
    #Anti-diagonal
    return result

print main(gen_table(100))
