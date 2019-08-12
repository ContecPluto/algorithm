import sys
sys.stdin = open('4012.txt','r')

T=int(input())
for num in range(1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result= 20000
    Alist, Blist=[],[]
    A_sum,B_sum = 0,0

    for set in range(1 << N):
        A, B = [], []
        for i in range(N):
            if set & (1 << i):
                A.append(i)
            else:
                B.append(i)
        if len(A) == len(B):
            Alist += [A]
            Blist += [B]

    print(Alist,Blist)







    # print(A,B)


    # print('#{} {}'.format(num, result))






            




