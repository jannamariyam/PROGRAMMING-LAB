def unique(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x