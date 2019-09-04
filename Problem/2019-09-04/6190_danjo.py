import sys; sys.stdin = open('6190.txt', 'r')

def backtrack(k, start):
    global result
    if k == R:
        multiply = choice[0] * choice[1]
        check_multiply = str(multiply)
        if len(check_multiply) > 1:
            for k in range(len(check_multiply)-1):
                if check_multiply[k] > check_multiply[k+1]:
                    break
            else:
                result = max(result, multiply)
    else:
        for i in range(start, N):
            choice[k] = arr[i]
            backtrack(k + 1, i + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = -1
    R = 2
    choice = [''] * R
    backtrack(0, 0)


    print('#{} {}'.format(tc, result))



