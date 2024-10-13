tri = [[0,0], [0,1,0]]
for i in range(2, 31):
    tri.append([0] + [tri[-1][j]+tri[-1][j+1] for j in range(i)] + [0])

r,c,w = map(int, input().split())

ans = 0
for i in range(r, r+w):
    for j in range(c, c+(i-r)+1):
        ans += tri[i][j]

print(ans)