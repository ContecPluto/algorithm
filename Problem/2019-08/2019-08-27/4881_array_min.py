import sys; sys.stdin = open('4881.txt', 'r')

def perm(k, s):
    global result
    if k == N:
        if result > s:
            result = s
        return
    elif result <= s:
        return
    else:
        #아직 선택되지 않은 요소들을 찾는다.
        for i in range(N):
            if order[i] == 0:
                order[i] = 1
                perm(k + 1, s + arr[k][i])
                order[i] = 0
        return



T = int(input())
for tc in range(1, T+1):
    #순열 합 -----------
    result = 1000
    N = int(input())
    order = [0 for _ in range(N)]
    arr = [list(map(int, input().split())) for i in range(N)]
    perm(0, 0)
    #순열 합 -------------- 결과값은 result를 이용해 사용함

    print('#{} {}'.format(tc, result))
