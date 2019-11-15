import sys; sys.stdin = open('4013.txt','r')

dx = [-1, 1]
check = [6, 2]
answer_list = [1, 2, 4, 8]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    answer = 0
    for i in range(N):
        origin, rotate = map(int, input().split())
        origin -= 1
        rotation = [[origin, rotate]]
        for x in range(2):
            teeth = origin
            tx = teeth + dx[x]
            while 0 <= tx < 4:
                if arr[teeth][check[x]] != arr[tx][check[x - 1]]:
                    if dx[x] == 1:
                        rotation.append([tx, rotation[-1][1] * -1])
                    else:
                        rotation.insert(0, [tx, rotation[0][1] * -1])
                else:
                    break
                teeth = tx + 0
                tx += dx[x]
        for idx, rotation_val in rotation:
            if rotation_val == -1:
                arr[idx].append(arr[idx].pop(0))
            else:
                arr[idx].insert(0, arr[idx].pop())
    for i in range(4):
        if arr[i][0] == 1:
            answer += answer_list[i]
    print('#{} {}'.format(tc, answer))