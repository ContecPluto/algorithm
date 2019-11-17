import sys; sys.stdin = open('5653.txt', 'r')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    crdnt = {}
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            crdnt[i, j] = [arr[i][j], 0]

    for times in range(2):
        copy_crdnt = {}
        for keys, values in crdnt.items():
            if times - values[1] == values[0] + 1:
                for i in range(4):
                    tx = keys[0] + dx[i]
                    ty = keys[1] + dy[i]
                    if crdnt.get((tx, ty)) != None: continue
                    if copy_crdnt.get((tx, ty)) != None:
                        if copy_crdnt.get((tx, ty))[0] < values[0]:
                            copy_crdnt[tx, ty] = [values[0], times]
                    else:
                        copy_crdnt[tx, ty] = [values[0], times]
        for k, v in copy_crdnt.items():
            crdnt[k] = v
    cnt = 0
    print(len(crdnt))
    for i in crdnt.values():
        if i[1] + i[0] >= K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))


