num, K = map(int, input().split())
twrs = []
twrs = list(map(int, input().split()))
dp = [0] * num
minT = twrs[0]
df = 0

for i in range(K - 1, num):
    df = 0
    minT = twrs[i]
    for j in range(K):
        df += twrs[i - j]
        minT = min(minT, twrs[i - j])
    df = df * minT
    df += dp[i - K]
    dp[i] = max(df, dp[i - 1] if K > 1 else df)
count = 0
answ = []
df = dp[i]
while i - K + 1 >= 0:
    if i == 0:
        count += 1
        answ.append(i + 1)
    if dp[i - 1] < df:
        count += 1
        answ.append(i - K + 2)
        i = i - K
        df = dp[i]
    else:
        i -= 1

print(count)
print(*answ[::-1])
