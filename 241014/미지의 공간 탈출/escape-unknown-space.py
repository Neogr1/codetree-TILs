from collections import deque

EAST,WEST,SOUTH,NORTH,TOP,BASE = 0,1,2,3,4,5
DIR = [(0,1), (0,-1), (1,0), (-1,0)]
ANOMALY = 9

def find_pos(board, target):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == target:
                return (i,j)
    return None

n,m,f = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
faces = [[list(map(int, input().split())) for _ in range(m)] for _ in range(5)]
anomaly = [tuple(map(int, input().split())) for _ in range(f)]

temp_r,temp_c = find_pos(board, 3)

# 3차원 그래프화
links = [[[[] for _ in range(m)] for _ in range(m)] for _ in range(5)] + [[[[] for _ in range(n)] for _ in range(n)]]
for i in range(m):
    links[TOP][0][i].append((NORTH,0,m-i-1))
    links[TOP][i][0].append((WEST,0,i))
    links[TOP][m-1][i].append((SOUTH,0,i))
    links[TOP][i][m-1].append((EAST,0,m-i-1))

    links[NORTH][0][i].append((TOP,0,m-i-1))
    links[WEST][0][i].append((TOP,i,0))
    links[SOUTH][0][i].append((TOP,m-1,i))
    links[EAST][0][i].append((TOP,m-i-1,m-1))

    links[NORTH][i][0].append((EAST,i,m-1))
    links[NORTH][i][m-1].append((WEST,i,0))
    links[WEST][i][0].append((NORTH,i,m-1))
    links[WEST][i][m-1].append((SOUTH,i,0))
    links[SOUTH][i][0].append((WEST,i,m-1))
    links[SOUTH][i][m-1].append((EAST,i,0))
    links[EAST][i][0].append((SOUTH,i,m-1))
    links[EAST][i][m-1].append((NORTH,i,0))

    if temp_r > 0:
        links[NORTH][m-1][i].append((BASE,temp_r-1,temp_c+(m-i-1)))
    if temp_c > 0:
        links[WEST][m-1][i].append((BASE,temp_r+i,temp_c-1))
    if temp_r+m < n:
        links[SOUTH][m-1][i].append((BASE,temp_r+m,temp_c+i))
    if temp_c+m < n:
        links[EAST][m-1][i].append((BASE,temp_r+(m-i-1),temp_c+m))

# 시간의 벽 그래프화
for r in range(m):
    for c in range(m):
        for dr,dc in DIR:
            nr = r+dr
            nc = c+dc
            if 0<=nr<m>nc>=0:
                for f in range(5):
                    links[f][r][c].append((f,nr,nc))

# 미지의 공간 그래프화
for r in range(n):
    for c in range(n):
        for dr,dc in DIR:
            nr = r+dr
            nc = c+dc
            if 0<=nr<n>nc>=0:
                links[BASE][r][c].append((BASE,nr,nc))



def update_time_anomaly(time):
    for r in range(n):
        for c in range(n):
            if anomaly_board[r][c] == None:
                continue
            d,v,trigger_time = anomaly_board[r][c]
            if time == trigger_time:
                anomaly_board[r][c] = None

                dr,dc = DIR[d]
                nr = r+dr
                nc = c+dc
                if 0 <= nr < n > nc >= 0 and board[nr][nc] in [0, ANOMALY]:
                    anomaly_board[nr][nc] = (d,v,time+v)
                    board[nr][nc] = ANOMALY


# 시간 이상의 위치 방향 주기 확산시간을 기록하는 배열
anomaly_board = [[None for _ in range(n)] for _ in range(n)]
for r,c,d,v in anomaly:
    anomaly_board[r][c] = (d,v,v)
    board[r][c] = ANOMALY

# 탐색
faces += [board]
check = [[[False for _ in range(m)] for _ in range(m)] for _ in range(5)] + [[[False for _ in range(n)] for _ in range(n)]]
start_r,start_c = find_pos(faces[TOP], 2)

time = 1
check[TOP][start_r][start_c] = True
positions = [(TOP,start_r,start_c)]
while positions:
    update_time_anomaly(time)

    new_positions = []
    for f,r,c in positions:
        for nf,nr,nc in links[f][r][c]:
            if faces[nf][nr][nc] == 4:
                print(time)
                exit(0)
            if not check[nf][nr][nc] and faces[nf][nr][nc] == 0:
                check[nf][nr][nc] = True
                new_positions.append((nf,nr,nc))

    positions = new_positions
    time += 1

print(-1)