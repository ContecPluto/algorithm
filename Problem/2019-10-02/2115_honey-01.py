import sys; sys.stdin =open('2115.txt','r')
sys.setrecursionlimit(9999999)


def comb(k, s):
    global result
    if k == 2:
        result_check = 0
        for honey_indexs in chose:
            n = len(honey_indexs)
            honey_check_squared = 1
            for subset in range(1 << n):
                check = []
                for j in range(n):
                    if subset & (1 << j):
                        check.append(arr[honey_indexs[j][0]][honey_indexs[j][1]])
                if sum(check) > C: continue
                honey_squared = 0
                for honey_index in check:
                    honey_squared += honey_index**2
                if honey_check_squared < honey_squared: honey_check_squared = honey_squared
            result_check += honey_check_squared
        result = max(result, result_check)
        return
    for i in range(s, N):
        if k > 0 and chose[k-1][-1][0] == lis[i][0][0] and chose[k-1][-1][1] >= lis[i][0][1]: continue
        chose.append(lis[i])
        comb(k + 1, i + 1)
        chose.pop()

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chose = []
    lis = []
    result = 0
    for i in range(N):
        for j in range(N-M+1):
            lis.append([[i, k] for k in range(j, j+M)])
    N = len(lis)
    comb(0, 0)
    print('#{} {}'.format(tc, result))
