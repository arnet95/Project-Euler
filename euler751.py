
def f(theta):
    s = ""
    b = float(theta)
    a = int(b)
    for i in range(15):
        s += str(a)
        b = a + a*(b - int(b))
        a = int(b)
    return theta[:26] == (s[0] + "." + s[1:])[:26], theta[:26]

print(f("2.223561019313554106173177192"))