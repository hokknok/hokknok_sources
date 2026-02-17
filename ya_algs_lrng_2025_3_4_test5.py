num, K = map(int, input().split())
twrs = []
twrs = list(map(int, input().split()))
dp = [0] * num
minT = twrs[0]
df = 0

for i in range(K):
    df += twrs[i]
    minT = min(minT, twrs[i])
dp[K - 1] = df * minT

for i in range(K, num):
    df = 0
    minT = twrs[i]
    for j in range(i, i - K, -1):
        df += twrs[j]
        minT = min(minT, twrs[j])
    df = df * minT
    df += dp[i - K]
    dp[i] = max(df, dp[i - 1] if K > 1 else df)

#print(dp)

count = 0
answ = []
df = dp[i]
while i - K + 1 >= 0:
    if i == 0:
        count += 1
        answ.append(i + 1)
        break
    if dp[i - 1] < df:
        count += 1
        answ.append(i - K + 2)
        i = i-K
        df = dp[i]
        continue
    i -= 1

print(count)
print(*answ[::-1])
