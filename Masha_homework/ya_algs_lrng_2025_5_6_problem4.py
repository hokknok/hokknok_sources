n, p = map(int, input().split())
lst = list(map(int, input().split()))
cur = []
for i in range(n):
    cur.append([i + 1, lst[i]])
cur = sorted(cur, key=lambda x: x[1])
i_ans, j_ans, best = 0, 0, cur[n - 1][1] * p

if n == 2:
    if abs(cur[0][1]/cur[1][1] - p) <= abs(cur[1][1]/cur[0][1] - p):
        print(cur[0][0],cur[1][0])
    else:
        print(cur[1][0], cur[0][0])
else:
    for i in range(n):
        l, r = 0, n - 1
        zn1,zn2,left,right = 0,0,0,0
        j_ans_l = 0
        i_best = best
        while l < r:
            m = (l + r) // 2
            if m == i:
                l += 1
                m += 1

            if n > m + 1 and m - 1 >= 0:
                zn1, zn2 = m - 1, m + 1
                left = abs(cur[i][1] * cur[zn2][1] - p * cur[zn1][1] * cur[zn2][1])
                right = abs(cur[i][1] * cur[zn1][1] - p * cur[zn1][1] * cur[zn2][1])
                if left > right:
                    if right < i_best:
                        j_ans_l = m + 1
                        i_best = right
                    l = m + 1
                else:
                    if left < i_best:
                        j_ans_l = m - 1
                        i_best = left
                    r = m
            else:
                if n == m + 1:
                    zn1, zn2 = m - 1, m
                elif  m - 1 == 0:
                    zn1, zn2 = m, m + 1
                left = abs(cur[i][1] * cur[zn2][1] - p * cur[zn1][1] * cur[zn2][1])
                right = abs(cur[i][1] * cur[zn1][1] - p * cur[zn1][1] * cur[zn2][1])
                if left > right:
                    if right < i_best:
                        j_ans_l = zn2
                        i_best = right
                    l = max(m, l + 1)
                else:
                    if left < i_best:
                        j_ans_l = zn1
                        i_best = left
                    #r = m
                    r = min(m, r - 1)
            if cur[i][0] == 7:
                print(cur[i][1], cur[j_ans_l][1])
        else:
            cur_m = abs(cur[i][1]/cur[j_ans_l][1] - p)
            if cur_m < best:
                best = cur_m
                i_ans, j_ans = cur[i][0], cur[j_ans_l][0]

    print(i_ans, j_ans)