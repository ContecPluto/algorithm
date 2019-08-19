import sys
sys.stdin = open('4408.txt','r')

T = int(input())

for num in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    check_1 = [0]*200
    for i, j in room:
        i = ((i + 1)/2) - 1 if i%2 else (i/2)-1
        j = ((j + 1)/2) - 1 if j%2 else (j/2)-1
        i, j = int(i), int(j)
        if i > j:  i, j = j, i
        for k in range(i, j+1):
            check_1[k] += 1
    print('#{} {}'.format(num, max(check_1)))



# for num in range(1, T+1):
#     count = 1
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#     check = []
#     for i, j in room:
#         if i in check or j in check:
#             count += 1
#         check =list(range(i,j+2))
#         # print(check) 
#     print('#{} {}'.format(num, count))





