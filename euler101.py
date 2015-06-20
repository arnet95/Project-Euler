#euler101 - Optimum polynomials
def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def gen_list(n):
    l = []
    for i in xrange(1,n+2):
        l.append([[i**k for k in xrange(n,-1,-1)],u(i)])
    return l

def solution(equations):
    coeff = equations[0][0]
    num = equations[0][1]
    if len(equations) == 1:
        return num/coeff[0]
    ret_list = []
    for i in xrange(1,n):
        list_in_question = equations[1]
        ret_list.append([        ,    ])
    return solution(ret_list)
