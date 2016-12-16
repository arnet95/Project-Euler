def test(n):

    print " "*(n+1) + "_"

    l = [1]
    for k in xrange(n):
        new_l = [1] + [(l[i]+l[i+1]) % 7 for i in xrange(0, k)] + [1]
        s = ""
        for i in new_l:
            s += ("*" if i == 0 else "_") + " "
        print " "*(n-k) + "%s" % s
        l = new_l

test(200)
