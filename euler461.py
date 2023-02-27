from math import pi, expm1, log2, log1p, floor, ceil

def f(n, k):
    return expm1(k/n)

def dist(r1, r2):
    return abs(r1-r2)

count = 0
test = 0

def naive_search(num_params, upper_limit, target, n):
    if num_params == 1:
        float_result = n*log1p(target)
        low = floor(float_result)
        high = ceil(float_result)
        if dist(f(n, low), target) < dist(f(n, high), target):
            return (low,)
        else:
            return (high,)
    else:
        low = floor(n*log1p(target/num_params))
        min_dist = dist(num_params*f(n, low), target)
        min_result = (low,)*num_params
        for last in range(low+1, upper_limit + 1):
            if num_params == 4:
                print(last)
            f_val = f(n, last)
            if f_val > target:
                if dist(target, f_val) < min_dist:
                    min_dist = dist(target, f_val)
                    min_result = (0,)*(num_params - 1) + (last,)
                break
            recursive_result = naive_search(num_params-1, last, target - f_val, n)
            result = sum(f(n,i) for i in recursive_result) + f_val
            if dist(result, target) < min_dist:
                min_dist = dist(result, target)
                min_result = recursive_result + (last,)
    return min_result


def main(n):
    return naive_search(4, 2*n, pi, n)

print(main(10000))