from eulertools import dynamic_sigma
import bisect

def gen_dT_list(n):
    sigma = dynamic_sigma(0, n+1)
    dT = [0]
    for i in xrange(1, n+1):
        if i % 2 == 0:
            dT.append(sigma[i//2]*sigma[i+1])
        else:
            dT.append(sigma[i]*sigma[(i+1)//2])
    return dT

def Tr(n):
    dT = gen_dT_list(n)
    #Create dictionary
    dT_vals = {}
    for i in xrange(1, n+1):
        dt = dT[i]
        if dt in dT_vals:
            dT_vals[dt].append(i)
        else:
            dT_vals[dt] = [i]
    key_vals = sorted(dT_vals.keys())
    lengths = {key: len(dT_vals[key]) for key in key_vals}
    result = 0
    for j in xrange(2, n):
        if j % 100 == 0:
            print j
        dtj = dT[j]
        app_point = bisect.bisect_left(key_vals, dtj)
        smaller_vals = key_vals[:app_point]
        smaller_count = 0
        for key in smaller_vals:
            smaller_count += (lengths[key] - bisect.bisect_right(dT_vals[key], j))
        larger_vals = key_vals[app_point+1:]
        larger_count = 0
        for key in larger_vals:
            larger_count += bisect.bisect_left(dT_vals[key], j)
        result += (smaller_count*larger_count)
    return result

print Tr(60*10**6)
