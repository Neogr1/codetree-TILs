def rotate(mat, r, c) -> None:
    mat[r-1][c-1],mat[r-1][c],mat[r-1][c+1],mat[r][c-1],mat[r][c],mat[r][c+1],mat[r+1][c-1],mat[r+1][c],mat[r+1][c+1] = (
        (
            mat[r+1][c-1],mat[r][c-1],mat[r-1][c-1],
            mat[r+1][c],mat[r][c],mat[r-1][c],
            mat[r+1][c+1],mat[r][c+1],mat[r-1][c+1],
        )
    )

def get_yumul_pos(mat):
    def dfs(mat,r,c,check):
        yumul_pos = [(r,c)]
        stack = [(r,c)]
        check[r][c] = 1
        while stack:
            r,c = stack.pop()
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<5>nc>=0 and check[nr][nc] == 0 and mat[r][c] == mat[nr][nc]:
                    yumul_pos.append((nr,nc))
                    stack.append((nr,nc))
                    check[nr][nc] = 1
        
        if len(yumul_pos) >= 3:
            return yumul_pos
        else:
            return []
                    
    
    yumul_pos = []
    check = [[0 for _ in range(5)] for _ in range(5)]
    for r in range(5):
        for c in range(5):
            yumul_pos.extend(dfs(mat, r, c, check))
    
    return yumul_pos


def eval_value(mat) -> int:
    return len(get_yumul_pos(mat))

def find_best_rotation(mat):
    max_value = 0
    rr = cc = dd = None
    for r in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                rotate(mat, r, c)
                value = eval_value(mat)
                if value > max_value:
                    max_value = value
                    rr,cc,dd = r,c,d
                elif value and value == max_value:
                    if d < dd:
                        rr,cc,dd = r,c,d
                    elif d == dd:
                        rr,cc = min((rr,cc), (r,c), key=lambda x:(x[1],x[0]))
            rotate(mat,r,c)

    return rr,cc,dd

def update_matrix(mat):
    yumul_pos = get_yumul_pos(mat)
    yumul_pos.sort(key=lambda x:(x[1],-x[0]))
    
    global no_index
    for r,c in yumul_pos:
        mat[r][c] = no[no_index]
        no_index = (no_index + 1) % m





k,m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(5)]
no = list(map(int, input().split()))
no_index = 0

for _ in range(k):
    r,c,d = find_best_rotation(mat)

    if r == c == d == None:
        break

    for _ in range(d):
        rotate(mat, r, c)

    total_value = 0
    while (value := eval_value(mat)):
        total_value += value
        update_matrix(mat)
    print(total_value, end=' ')