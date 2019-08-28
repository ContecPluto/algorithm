def tournament(v):
    # print('v=', v)
    winner = []
    if len(v) > 1:
        for i in range(0, len(v), 2):
            # print(i)
            if v[i+1:i+2]:
                if v[i][0] == 1:
                    if v[i+1][0] == 1 or v[i+1][0] == 3:
                        winner.append(v[i])
                    else:
                        winner.append(v[i+1])
                if v[i][0] == 2:
                    if v[i+1][0] == 2 or v[i+1][0] == 1:
                        winner.append(v[i])
                    else:
                        winner.append(v[i + 1])
                if v[i][0] == 3:
                    if v[i+1][0] == 3 or v[i+1][0] == 2:
                        winner.append(v[i])
                    else:
                        winner.append(v[i + 1])
                # print('위너1', winner)
            else:
                # print('위너2', v[i])
                # print(winner)
                winner.append(v[i])
        # print('인풋', winner)
        tournament(winner)
    # print(v)
    else:
        check.append(v[0])

def devison(list):

import sys; sys.stdin = open('4880.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    check = []
    n = int(input())
    student = list(map(list, input().split()))
    for i in range(len(student)):
        student[i][0] = int(student[i][0])
        student[i].append(i+1)
    # print(student)
    #
    # if len(st)
    # print(student[:(len(student)+1)//2])
    # print(student[((len(student)+1)//2)::])
    left = tournament(student[:(len(student)//2+1)])
    right = tournament(student[(len(student)//2)+1::])
    # print(check)
    tournament(check)
    print('#{} {}'.format(tc, check[len(check)-1][1]))
