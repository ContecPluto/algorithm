import sys
sys.stdin = open('4408.txt','r')

T = int(input())

for num in range(1, T+1):
    count = 1
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    check_1 = [0]*200
    for i, j in room:
        i = int(((i + 1)/2) - 1) if i%2 else int(i/2)
        j = int(((j + 1)/2) - 1) if j%2 else int(j/2)
        print(i,j)
    #     if i > j:
    #         i, j = j, i
    #     for k in range(i, j + 1):
    #         if check_1[k] == 1:
    #             check_1 = [0]*200
    #             count += 1
    #             break
    #     for k in range(i, j+1):
    #         check_1[k] = 1
    # print('#{} {}'.format(num, count))


        









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






# for num in range(1, T+1):
#     count = 1
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N-1):
#         for j in range(len(room[0])):
#             if room[i][j] > room[i+1][0]:
#                 count += 1
#                 break
#     print('#{} {}'.format(num, count))

