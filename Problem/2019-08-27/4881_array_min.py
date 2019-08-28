import sys; sys.stdin = open('4881.txt', 'r')

def perm(k, n, visit):   #visit: 지금까지 선택한 요소들의 집합
    global result
    if k == n:
        check = []
        for i in range(N):
            check.append(arr[order[i]])
        result.append(check)
    else:
        #아직 선택되지 않은 요소들을 찾는다.
        for i in range(n):
            if visit & (1 << i): continue
            order[k] = i
            perm(k + 1, n, visit | (1 << i))


T = int(input())
for tc in range(1, T+1):
    #부분 합 -----------
    result = []
    N = int(input())
    arr = list(range(N))
    order = [0] * N
    perm(0, N, 0)
    #부분 합 -------------- 결과값은 result를 이용해 사용함

    total = 0
    min_arr = 100000

    # print(result)
    arr2 = [list(map(int, input().split())) for i in range(N)]
    # print(arr2)
    for x in range(len(arr2)):
        for i in result:
            total = 0
            for j in i:
                # print(x,i[j])
                # print(arr2[x][i[j]])
                total += arr2[j][i[j]]
            # print(total)
            min_arr = min(total, min_arr)
    print('#{} {}'.format(tc, min_arr))
