def decode(c):
    a = ['w', 'g', 'b', 'o', 'p', 'j', 'q', 'd', 'e', 'z', 'n', 's', 'h', 'v', 'k', 'r', 'c', 'y', 'f', 'x', '+', 't', 'l', 'm', 'u', 'a', 'i']
    dd = {136:'impossible',61:'easy',59:'hard',98:'normal'}
    try:
        d1 = int(c[0:3])
    except:
        print('invalid code')
        return False,None,None
    s1 = c[3:]
    p = 0
    s2 = 0
    for x in reversed(s1):
        m = a.index(x)
        s2 += m*(26**p)
        p += 1

    for x in range(1,7):
        if d1/x in list(dd.keys()):
            d1 = d1/x
            break
    else:
        print('invalid code')
        return False,None,None

    d2 = dd.get(d1)
    return(True, s2, d2)