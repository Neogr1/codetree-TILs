from copy import deepcopy

def left(board):
    for r in range(n):
        new = [0]*n
        pos = 0
        for c in range(n):
            if board[r][c] != 0:
                if new[pos] == 0:
                    new[pos] = board[r][c]
                elif new[pos] == board[r][c]:
                    new[pos] *= 2
                    pos += 1
                else:
                    pos += 1
                    new[pos] = board[r][c]
        for c in range(n):
            board[r][c] = new[c]
        

def right(board):
    for r in range(n):
        new = [0]*n
        pos = n-1
        for c in range(n-1,-1,-1):
            if board[r][c] != 0:
                if new[pos] == 0:
                    new[pos] = board[r][c]
                elif new[pos] == board[r][c]:
                    new[pos] *= 2
                    pos -= 1
                else:
                    pos -= 1
                    new[pos] = board[r][c]
        for c in range(n-1,-1,-1):
            board[r][c] = new[c]

def up(board):
    for c in range(n):
        new = [0]*n
        pos = 0
        for r in range(n):
            if board[r][c] != 0:
                if new[pos] == 0:
                    new[pos] = board[r][c]
                elif new[pos] == board[r][c]:
                    new[pos] *= 2
                    pos += 1
                else:
                    pos += 1
                    new[pos] = board[r][c]
        for r in range(n):
            board[r][c] = new[r]

def down(board):
    for c in range(n):
        new = [0]*n
        pos = n-1
        for r in range(n-1,-1,-1):
            if board[r][c] != 0:
                if new[pos] == 0:
                    new[pos] = board[r][c]
                elif new[pos] == board[r][c]:
                    new[pos] *= 2
                    pos -= 1
                else:
                    pos -= 1
                    new[pos] = board[r][c]
        for r in range(n-1,-1,-1):
            board[r][c] = new[r]

def find_maximum_score(board, move_left):
    if move_left == 0:
        return max(max(i) for i in board)
    else:
        left(lb := deepcopy(board))
        right(rb := deepcopy(board))
        up(ub := deepcopy(board))
        down(db := deepcopy(board))
        l = find_maximum_score(lb, move_left-1)
        r = find_maximum_score(rb, move_left-1)
        u = find_maximum_score(ub, move_left-1)
        d = find_maximum_score(db, move_left-1)
        return max(l,r,u,d)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print(find_maximum_score(board, 5))