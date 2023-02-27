def F(d):
    count = [4, 3, 3]
    data = {(1, (1, 0, 0)): 3, (0, (0, 1, 0)): 3, (0, (0, 0, 1)): 3}
    for k in range(2, d+1):
        new_data = {}
        for data_point in data:
            a, bs = data_point
            for m in range(3):
                new_a = (a + bs[(-m)%3] + (m == 0)) % 3
                new_bs = [bs[(i-m)%3] for i in range(3)]
                new_bs[m] += 1
                new_bs = [i % 3 for i in new_bs]
                new_data_point = (new_a, tuple(new_bs))
                if new_data_point in new_data:
                    new_data[new_data_point] += count[m]*data[data_point]
                else:
                    new_data[new_data_point] = count[m]*data[data_point]
        data = {val: new_data[val] % (10**9+7) for val in new_data}
    print(sum(data[val] for val in data if val[0] == 0))

F(10**5)