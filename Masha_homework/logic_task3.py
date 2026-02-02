def A(x):
    return x+2
def B(x):
        return x+3
def C(x):
    return x*5

ind = 0
funcs = [A, B, C]

def brutal_force(prev, prgrm):
    global ind
    for func in funcs:
        nxt = func(prev[-1])

        if nxt > 35 or nxt == 21 or (nxt > 6 and prev[-1] < 6):
            continue

        if nxt == 35:
            ind += 1
            print(prev + [nxt])
            print(prgrm + func.__name__)
            print()
            continue
        brutal_force(prev + [nxt], prgrm + func.__name__)

brutal_force([1],'')
print(ind)



