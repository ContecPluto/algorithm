# 문자	수행 명령
# <	이동 방향을 왼쪽으로 바꾼다.
# >	이동 방향을 오른쪽으로 바꾼다.
# ^	이동 방향을 위쪽으로 바꾼다.
# v	이동 방향을 아래쪽으로 바꾼다.
# _	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
# |	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
# ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
# .	아무 것도 하지 않는다.
# @	프로그램의 실행을 정지한다.
# 0~9	메모리에 문자가 나타내는 값을 저장한다.
# +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
# -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.

import sys; sys.stdin = open('1824.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def Verification(t, move, memori, counter):
    global answer
    x, y = t
    if answer == 'YES' or counter >= 900:
        return
    if arr[x][y].isdigit():
        tx = x + dx[move]
        ty = y + dy[move]
        if tx == R:
            tx = 0
        elif tx == -1:
            tx = R - 1
        if ty == C:
            ty = 0
        elif ty == -1:
            ty = C - 1
        Verification([tx, ty], move, int(arr[x][y]), counter+1)
    else:
        if arr[x][y] == '>': move = 3
        elif arr[x][y] == '<': move = 2
        elif arr[x][y] == '^': move = 0
        elif arr[x][y] == 'v': move = 1
        elif arr[x][y] == '+':
            if memori == 15:
                memori = 0
            else:
                memori += 1
        elif arr[x][y] == '-':
            if memori == 0:
                memori = 15
            else:
                memori -= 1
        elif arr[x][y] == '_':
            if memori == 0:
                move = 3
            else:
                move = 2
        elif arr[x][y] == '|':
            if memori == 0:
                move = 1
            else:
                move = 0
        elif arr[x][y] == '?':
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if tx == R:
                    tx = 0
                elif tx == -1:
                    tx = R - 1
                if ty == C:
                    ty = 0
                elif ty == -1:
                    ty = C - 1
                if not i in history[tx][ty]:
                    history[tx][ty].append(i)
                    Verification([tx, ty], i, memori, counter+1)
            return
        elif arr[x][y] == '@':
            answer = 'YES'
            return
        tx = x + dx[move]
        ty = y + dy[move]
        if tx == R:
            tx = 0
        elif tx == -1:
            tx = R - 1
        if ty == C:
            ty = 0
        elif ty == -1:
            ty = C - 1
        Verification([tx, ty], move, memori, counter+1)

T = int(input())
for tc in range(1, T+1):
    counter = 0
    answer = 'NO'
    R, C = map(int, input().split())
    history = [[[] for _ in range(C)] for _ in range(R)]
    arr = [input() for _ in range(R)]
    Verification([0, 0], 3, 0, 0)
    print('#{} {}'.format(tc, answer))
