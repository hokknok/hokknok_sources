n = int(input())
tree = [[] for _ in range(n + 1)]
ans = n - 1
for i in range(n - 1):
    fst, scn = map(int, input().split())
    tree[fst].append(scn)
    tree[scn].append(fst)
tails = [[] for _ in range(n + 1)]
tail_parent = [0] * (n + 1)
qeue = []
i = min(range(1, len(tree)), key=lambda i: len(tree[i]))
while n > 0:
    if len(tree[i]) > 0:
        qeue.append(i)
        if len(tails[i]) == 0:
            tp = tail_parent[i]
        else:
            loc_min = min(tails[i])
            tp = loc_min if loc_min < tail_parent[i] else tail_parent[i]
        prev = i
        i = tree[i][0]
        tree[i].remove(prev)
        tree[prev].remove(i)
        tail_parent[i] = tp + 1
    else:
        n -= 1
        if n > 0:
            tp = 0 if len(tails[i]) == 0 else min(tails[i])
            tails[i].append(tail_parent[i])
            tails[i] = sorted(tails[i])
            ans = min(ans, sum(tails[i][0:2]))
            i = qeue.pop()
            tails[i].append(tp + 1)
            tails[i] = sorted(tails[i])
            tails[i] = tails[i][0:min(len(tails[i]), 2)]
print(ans)
