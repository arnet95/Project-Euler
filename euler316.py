def prefix(sub, s):
    return s[:len(sub)] == sub

def g(n):
    s = str(n)
    result_str = ""
    for i in xrange(len(s)):
        if prefix(s[i:], s):
            result_str += "1"
        else:
            result_str += "0"
    return 10*int(result_str) - (len(s)-1)

def main(N):
    result = 0
    for n in xrange(2, N):
        result += g(10**16//n)
    return result

print main(10**6)
