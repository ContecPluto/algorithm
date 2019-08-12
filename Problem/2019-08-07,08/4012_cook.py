import sys
sys.stdin = open('4012.txt','r')

T=int(input())
for num in range(1,T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result= 20000
    A_sum,B_sum = 0,0

    for set in range(1 << N):
        A, B = [], []
        for i in range(N):
            if set & (1 << i):
                A.append(i)
            else:
                B.append(i)
        if len(A) == len(B):
            for x in range(len(A)):
                for y in range(len(A)):
                    if x !=y:
                        A_sum += table[A[x]][A[y]]
                        B_sum += table[B[x]][B[y]]
            dif = abs(A_sum - B_sum)
            A_sum,B_sum = 0,0            
            result = dif if result > dif else result
    print('#{} {}'.format(num, result))












            




