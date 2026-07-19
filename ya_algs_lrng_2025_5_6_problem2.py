n = int(input())
tree = [[] for _ in range(n + 1)]
ans = n - 1

for i in range(n - 1):
    fst, scn = map(int, input().split())
    tree[fst].append(scn)
    tree[scn].append(fst)

def recrs(id, tail1, ex):
    global ans
    tail2, tail_rtrn = 10 ** 5, 10 ** 5
    for each in tree[id]:
        if each != ex:
            tail2 = min(tail2, recrs(each, tail1 + 1, id))
            tail_rtrn = min(tail_rtrn, tail2)
            tail1, tail2 = min(tail1, tail2), max(tail2, tail1)
    if tail2 == 10 ** 5:
        tail2 = tail1
        tail1, tail_rtrn = 0,0
    ans = min(ans, tail1 + tail2)
    return tail_rtrn + 1


start = min(range(1, len(tree)), key=lambda i: len(tree[i]))
recrs(start, 0, 0)

print(ans)
