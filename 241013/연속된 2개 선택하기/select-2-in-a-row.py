n = int(input())
arr = list(map(int, input().split()))

dp = [[0,0,0] for _ in range(n)]
dp[0][1] = arr[0]
for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]

print(max(dp[n-1]))