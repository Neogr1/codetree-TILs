import sys
input = sys.stdin.readline

n,k = map(int, input().split())
values = [int(input()) for _ in range(n)]

counts = [k+1] * (k+1)
counts[0] = 0
for i in range(1, k+1):
    for v in values:
        if i-v >= 0:
            counts[i] = min(counts[i], counts[i-v]+1)

print(counts[k]if counts[k] != k+1 else -1)