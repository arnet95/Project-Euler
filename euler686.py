powertwenty = 1
i = 0
count = 0
while True:
    powertwenty *= 2
    s = str(powertwenty)
    i += 1
    if s[:3] == "123":
        count += 1
        if count % 1000 == 0:
            print(count)
        if count == 678910:
            print(i)
            break
    powertwenty = int(s[:20])