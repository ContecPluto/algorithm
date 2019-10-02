import sys; sys.stdin =open('2115.txt','r')

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
                        check.append(honey_indexs[j])
                honey_middle_check = 0
                honey_squared = 0
                for honey_index in check:

                    honey_middle_check += arr[honey_index[0]][honey_index[1]]
                    if honey_middle_check > C: break
                    honey_squared += arr[honey_index[0]][honey_index[1]]**2
                else:
                    if honey_check_squared < honey_squared:
                        honey_check_squared = honey_squared
            result_check += honey_check_squared
        result = max(result, result_check)
        return
    for i in range(s, N):
        if k > 0:
            if chose[-1][-1][0] == lis[i][0][0]:
                if chose[-1][-1][1] >= lis[i][0][1]:
                    continue
        chose.append(lis[i])
        comb(k + 1, i + 1)
        chose.pop()
T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chose = []
    lis = []
    result = 0
    for i in range(N):
        for j in range(N-M+1):
            lis.append(tuple([(i, k) for k in range(j, j+M)]))
    N = len(lis)
    comb(0, 0)
    print('#{} {}'.format(tc, result))
