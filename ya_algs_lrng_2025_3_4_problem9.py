# n, m = map(int, input().split())
# mtrx = []
# dfs = []
# dp = [[0] * m for _ in range(n)]
# answ = 0


# def check_node(i, j):
#     mx = 1
#     if j - 1 > -1 and mtrx[i][j - 1] - mtrx[i][j] == 1:
#         if dp[i][j - 1] == 0:
#             dp[i][j - 1] = check_node(i, j - 1)
#         mx = max(mx, 1 + dp[i][j - 1])
#     if j + 1 < m and mtrx[i][j + 1] - mtrx[i][j] == 1:
#         if dp[i][j + 1] == 0:
#             dp[i][j + 1] = check_node(i, j + 1)
#         mx = max(mx, 1 + dp[i][j + 1])
#     if i - 1 > -1 and mtrx[i - 1][j] - mtrx[i][j] == 1:
#         if dp[i - 1][j] == 0:
#             dp[i - 1][j] = check_node(i - 1, j)
#         mx = max(mx, 1 + dp[i - 1][j])
#     if i + 1 < n and mtrx[i + 1][j] - mtrx[i][j] == 1:
#         if dp[i + 1][j] == 0:
#             dp[i + 1][j] = check_node(i + 1, j)
#         mx = max(mx, 1 + dp[i + 1][j])
#
#     return mx
#
# def regress():
#     for i in range(n):
#         line = list(map(int, input().split()))
#         mtrx.append(line)
#
#     for i in range(n):
#         for j in range(m):
#             if dp[i][j] == 0:
#                 dp[i][j] = check_node(i, j)
#     print(max(max(row) for row in dp))


def check_node(i, j):
    vrs = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
    for k in vrs:
        ni, nj = k[0], k[1]
        if ni >= n or ni < 0 or nj >= m or nj < 0:
            continue
        if mtrx[ni][nj] - mtrx[i][j] == -1:
            dfs.append(k)


# def dfs():
#     for i in range(n):
#         line = list(map(int, input().split()))
#         mtrx.append(line)
#     dfs = []
#
#     for i in range(n):
#         for j in range(m):
#             if dp[i][j] == 0:
#                 dp[i][j] = -1
#                 dfs.append([i, j])
#                 check_node(i, j)
#                 while len(dfs) > 0:
#                     row, col = dfs[len(dfs) - 1]
#                     if dp[row][col] != -1:
#                         dp[row][col] = -1
#                         check_node(row, col)
#                     else:
#                         if col > 0 and mtrx[row][col - 1] - mtrx[row][col] == 1:
#                             dp[row][col] = max(dp[row][col - 1], dp[row][col])
#                         if col + 1 < m and mtrx[row][col + 1] - mtrx[row][col] == 1:
#                             dp[row][col] = max(dp[row][col + 1], dp[row][col])
#                         if row > 0 and mtrx[row - 1][col] - mtrx[row][col] == 1:
#                             dp[row][col] = max(dp[row - 1][col], dp[row][col])
#                         if row + 1 < n and mtrx[row + 1][col] - mtrx[row][col] == 1:
#                             dp[row][col] = max(dp[row + 1][col], dp[row][col])
#                         dp[row][col] = max(1, 1 + dp[row][col])
#                         answ = max(answ, dp[row][col])
#                         dfs.pop()
#
#     print(answ)


# def big_small():
#     global answ
#     vl_crd = {}
#     for i in range(n):
#         line = list(map(int, input().split()))
#         mtrx.append(line)
#         for j, val in enumerate(line):
#             if val in vl_crd:
#                 vl_crd[val].append([i, j])
#             else:
#                 vl_crd[val] = [[i, j]]
#     vl_crd = dict(sorted(vl_crd.items(), reverse=True))
#
#     keys = sorted(vl_crd)
#     dpp = {}
#     dpp[keys[0]] = 1
#
#     for prev_k, cur_k in zip(keys, keys[1:]):
#         if cur_k - prev_k == 1:
#             dpp[cur_k] = dpp.get(prev_k, 0) + 1
#         else:
#             dpp[cur_k] = 1
#
#     dpp = dict(sorted(dpp.items(), key=lambda itm: itm[1], reverse=True))
#     while len(vl_crd) > 0:
#         for kk, vv in dpp.items():
#             if vv <= answ:
#                 print(answ)
#                 return
#             v = vl_crd[kk]
#             for each in v:
#                 i, j = each
#                 dp[i][j] = -1
#                 dfs.append([i, j])
#                 check_node(i, j)
#                 while len(dfs) > 0:
#                     row, col = dfs[len(dfs) - 1]
#                     if dp[row][col] != -1:
#                         dp[row][col] = -1
#                         check_node(row, col)
#                     else:
#                         if col > 0 and mtrx[row][col - 1] - mtrx[row][col] == -1:
#                             dp[row][col] = max(dp[row][col - 1], dp[row][col])
#                         if col + 1 < m and mtrx[row][col + 1] - mtrx[row][col] == -1:
#                             dp[row][col] = max(dp[row][col + 1], dp[row][col])
#                         if row > 0 and mtrx[row - 1][col] - mtrx[row][col] == -1:
#                             dp[row][col] = max(dp[row - 1][col], dp[row][col])
#                         if row + 1 < n and mtrx[row + 1][col] - mtrx[row][col] == -1:
#                             dp[row][col] = max(dp[row + 1][col], dp[row][col])
#                         dp[row][col] = max(1, 1 + dp[row][col])
#                         answ = max(answ, dp[row][col])
#                         dfs.pop()
#         vl_crd.pop(kk)
#         dpp.pop(kk)
#
#     print(answ)

def max_2_min():
    n, m = map(int, input().split())
    mtrx, vij = [], []
    dp = [[0] * m for _ in range(n)]
    answ = 1
    start = 0
    for i in range(n):
        line = list(map(int, input().split()))
        mtrx.append(line)
        for j in range(m):
            vij.append([line[j], i, j])
    vij = sorted(vij, reverse=True)

    for k in range(n*m):
        dp[vij[k][1]][vij[k][2]] = 1
        if k + 1 < m and vij[k + 1] != vij[k]:
            start = k + 1
            break

    for k in range(start, n*m):
        i, j = vij[k][1], vij[k][2]
        vrs = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
        for k in vrs:
            ni, nj = k[0], k[1]
            if ni >= n or ni < 0 or nj >= m or nj < 0:
                continue
            if mtrx[ni][nj] - mtrx[i][j] == 1:
                dp[i][j] = max(dp[i][j], 1 + dp[ni][nj])
                answ = max(answ, dp[i][j])
        dp[i][j] = max(dp[i][j], 1)

    print(answ)

if __name__ == '__main__':
    # regress()
    # dfs()
    #big_small()
    max_2_min()
