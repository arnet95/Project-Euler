t_mem = {}
s_mem = {1: 1, 2: 1, 3: 1, 4: 2}

def s(n):
    "Number of palindromes summing to n which do not contain 2"
    if n in s_mem:
        return s_mem[n]
    else:
        result = 2 - (n % 2)
        if n % 2 == 1:
            i = 1
            while n - 2*i > 0:
                if i != 2:
                    result += s(n-2*i)
                i += 1
        else:
            i = 1
            while n - 2*i > 0:
                if i != 2:
                    result += s(n-2*i)
                i += 1
        s_mem[n] = result
        return result

i = 44
mod = 10**6
total = pow(2, 22, mod)
s_list = [s(i - 6), s(i - 4), s(i-2), s(i)]
t = (total - s_list[-1]) % mod
while t != 0:
    total = (total * 2) % mod
    s_list = s_list[1:] + [(s_list[0] + s_list[2] + s_list[3]) % mod]
    t = (total - s_list[-1]) % mod
    i += 2
print(i)
