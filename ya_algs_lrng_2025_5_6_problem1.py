a, b, S = map(int, (input().split()))
x = 0
if a != b:
    aa, bb, cc = 1, abs(a - b), -S
    D = pow(bb, 2) - 4 * aa * cc
    x = (-bb + pow(D, 0.5))/2
    if isinstance(x, complex):
        print(-1)
    elif int(x) > 0 and x - int(x) == 0:
        print(int(x) + max(a, b))
    else:
        print(-1)
else:
    x = pow(S, 0.5)
    if isinstance(x, complex):
        print(-1)
    elif x - int(x) == 0:
        print(int(x) + a)
    else:
        print(-1)