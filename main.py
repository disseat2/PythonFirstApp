def charfrq(str):
    dct = {}
    for k in str:
        keys = dct.keys()
        if k in keys:
            dct[k] += 1
        else:
            dct[k] = 1
    return dct
print(charfrq("Test_test"))