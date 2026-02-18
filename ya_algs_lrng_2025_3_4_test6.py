rd, ln, dp = [], [], []
maxw = -1
def calc_coin(k, s, e, i):
    global rd, ln, dp, maxw
    if ln[k] >= 0:
        for j in range(s, e+1):
            dp[i][k] = max(dp[i][k], ln[k] + dp[i - 1][j] if dp[i - 1][j] >= 0 else dp[i - 1][j])
    else:
        maxw = max(maxw, dp[i - 1][0])
def main():
    global rd, ln, dp, maxw
    n = int(input())
    for i in range(n):
        rd.append(input())
    dp = [[-1, -1, -1] for _ in range(n)]
    dic = {'W': -1, 'C': 1, '.': 0}
    dp[0] = [dic[c] for c in rd[0]]
    for i in range(1, n):
        ln = [dic[c] for c in rd[i]]
        dicL = {0: (0,1), 1: (0,2), 2: (1,2)}
        for k,(s,e) in dicL.items():
            calc_coin(k, s, e, i)
        if dp[i] == [-1, -1, -1]:
            i -= 1
            break
    print(max(max(dp[i]), maxw, 0))

if __name__ == '__main__':
    main()
