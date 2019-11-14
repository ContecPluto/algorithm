import sys; sys.stdin = open('4012.txt','r')

def comb(k, s):
    global result
    if s == end:
        A_sum, B_sum = 0, 0
        B = list(origin - set(A))
        for x in range(len(A)):
            for y in range(len(A)):
                A_sum += table[A[x]][A[y]]
                B_sum += table[B[x]][B[y]]
        result = min(result, abs(A_sum - B_sum))
        return
    for i in range(k, N):
        A.append(i)
        comb(i + 1, s + 1)
        A.pop()

T=int(input())
for num in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result = 20000
    end = N//2
    origin = set(range(N))
    A = []
    comb(0, 0)
    print('#{} {}'.format(num, result))

