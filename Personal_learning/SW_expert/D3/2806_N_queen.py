import sys; sys.stdin = open('2806.txt', 'r')
def Possible(k, c): #k번  퀸의 열 1가 답이 되는 선택인지 조사
    for i in range(k): #0~ k-1 번 퀸과 대각선에 있는지 조사
        if k - i == abs(arr[c] - arr[i]):
            return False
    return True
def per(a):
    global answer
    if a == N:
        answer += 1
        return
    for i in range(a, N):
        if not Possible(a, i): continue
        arr[i], arr[a] = arr[a], arr[i]
        per(a + 1)
        arr[i], arr[a] = arr[a], arr[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(range(N))
    answer = 0
    per(0)
    print('#{} {}'.format(tc, answer))