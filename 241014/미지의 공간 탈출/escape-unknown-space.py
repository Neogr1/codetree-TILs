from collections import deque

east,west,south,north,top = 0,1,2,3,4
DIR = [(0,1), (0,-1), (1,0), (-1,0)]

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

# 시간 벽 탈출 지점 찾기
links = [[[[] for _ in range(m)] for _ in range(m)] for _ in range(5)]
for i in range(m):
    links[top][0][i].append((north,0,m-i-1))
    links[top][i][0].append((west,0,i))
    links[top][m-1][i].append((south,0,i))
    links[top][i][m-1].append((east,0,m-i-1))

    links[north][0][i].append((top,0,m-i-1))
    links[west][0][i].append((top,i,0))
    links[south][0][i].append((top,m-1,i))
    links[east][0][i].append((top,m-i-1,m-1))

    links[north][i][0].append((east,i,m-1))
    links[north][i][m-1].append((west,i,0))
    links[west][i][0].append((north,i,m-1))
    links[west][i][m-1].append((south,i,0))
    links[south][i][0].append((west,i,m-1))
    links[south][i][m-1].append((east,i,0))
    links[east][i][0].append((south,i,m-1))
    links[east][i][m-1].append((north,i,0))

check = [[[False for _ in range(m)] for _ in range(m)] for _ in range(5)]
sr,sc = find_pos(faces[top], 2)
q = deque([(top,sr,sc,0)])
while q:
    face,r,c,dis = q.popleft()
    if face != top and r == m-1:
        break
    
    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r+dr
        nc = c+dc
        if 0<=nr<m>nc>=0 and faces[face][nr][nc] == 0 and not check[face][nr][nc]:
            check[face][nr][nc] = True
            q.append((face,nr,nc,dis+1))
    for nf,nr,nc in links[face][r][c]:
        if faces[nf][nr][nc] == 0 and not check[nf][nr][nc]:
            check[nf][nr][nc] = True
            q.append((nf,nr,nc,dis+1))

face,row,col,dis = face,r,c,dis
        


# 시간 이상 업데이트
def update_time_anomaly(t):
    for r in range(n):
        for c in range(n):
            if ano_board[r][c] == None:
                continue
            d,v,trigger_time = ano_board[r][c]
            if t == trigger_time:
                ano_board[r][c] = None

                dr,dc = DIR[d]
                nr = r+dr
                nc = c+dc
                if 0 <= nr < n > nc >= 0 and board[nr][nc] in [0, 9]:
                    ano_board[nr][nc] = (d,v,t+v)
                    board[nr][nc] = 9

ano_board = [[None for _ in range(n)] for _ in range(n)]
for r,c,d,v in anomaly:
    ano_board[r][c] = (d,v,v)
    board[r][c] = 9

for t in range(dis+1):
    update_time_anomaly(t)

# 최종 탈출 + 시간 이상 업데이트
tr,tc = find_pos(board, 3)
if face == east:
    row,col = tr+(m-col-1),tc+m
elif face == west:
    row,col = tr+col,tc-1
elif face == south:
    row,col = tr+m,tc+col
else:
    row,col = tr-1,tc+(m-col-1)

dis += 1
update_time_anomaly(dis)

if not 0<=row<n>col>=0 or not board[row][col] in [0,4]:
    print(-1)
    exit(0)
if board[row][col] == 4:
    print(dis)
    exit(0)

check = [[0 for _ in range(n)] for _ in range(n)]
check[row][col] = 1
pos_list = [(row,col)]
while pos_list:
    dis += 1
    update_time_anomaly(dis)


    next_pos_list = []
    for r,c in pos_list:
        
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = r+dr
            nc = c+dc
            if 0<=nr<n>nc>=0 and board[nr][nc] in [0,4] and not check[nr][nc]:
                if board[nr][nc] == 4:
                    print(dis)
                    exit(0)
                next_pos_list.append((nr,nc))
                check[nr][nc] = 1

    pos_list = next_pos_list

print(-1)