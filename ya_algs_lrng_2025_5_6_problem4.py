# n, p = map(int, input().split())
# lst = list(map(int, input().split()))
# cur = []
# for i in range(n):
#     cur.append([i + 1, lst[i]])
# cur = sorted(cur, key=lambda x: x[1])
# ans_i, ans_j = 0, 0
# gl_chm = max(p, cur[n - 1][1])
#
# for i in range(n):
#     l, r = 0, n - 1
#     chm = cur[i][1] * p
#     while l <= r:
#         m = (l + r) // 2
#         if cur[m][1] == chm:
#             break
#         elif cur[m][1] < chm:
#             l = m + 1
#         else:
#             r = m - 1
#     m1 = m2 = m3 = 10**19
#     if m != 0:
#         m1 = abs(cur[m - 1][1] - chm)
#     if m != n - 1:
#         m3 = abs(cur[m + 1][1] - chm)
#     if i != m:
#         m2 = abs(cur[m][1] - chm)
#     mn = min(m1, m2, m3)
#     if mn == m1:
#         m -= 1
#     elif mn == m3:
#         m += 1
#     gl_chn = abs(cur[m][1] / cur[i][1] - p)
#     if gl_chn < gl_chm:
#         gl_chm = gl_chn
#         ans_i, ans_j = m, i
# print(cur[ans_i][0], cur[ans_j][0])
from bisect import bisect_left

n, p = map(int, input().split())
a = list(map(int, input().split()))
cur = sorted((a[i], i + 1) for i in range(n))
vals = [v for v, _ in cur]

best = None
ans_i = ans_j = 0

for j, (cj, j_id) in enumerate(cur):
    target = cj * p
    k = bisect_left(vals, target)
    best_idx = None
    best_dist = None
    for idx in (k - 2, k - 1, k, k + 1):
        if 0 <= idx < n and idx != j:
            dist = abs(vals[idx] - target)
            if best_dist is None or dist < best_dist:
                best_dist = dist
                best_idx = idx
    ci = vals[best_idx]
    # |ci/cj - p| = |ci - p*cj| / cj
    score = (abs(ci - target), cj)  # сравнение как дроби: меньше score лучше
    if best is None or score[0] * best[1] < best[0] * score[1]:
        best = score
        ans_i, ans_j = cur[best_idx][1], j_id

print(ans_i, ans_j)
