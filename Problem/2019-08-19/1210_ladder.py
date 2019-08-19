


import sys
sys.stdin = open('1210.txt', 'r')

for num in range(1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    ladder_index = [[] for _ in range(100)]
    for x in range(100):
        for y in range(100):
            if ladder[x][y]:
                ladder_index[x].append(y)
    # for x in range(100):
    #     print(x, '-->', ladder_index[x])

    visit = [[False] * 100] * 100
    for x in range(1):
        for y in ladder_index[x]:
            print(x,y)
            visit[x][y] = True
    print(visit[0])





# def DFS(v):
#     visit[0][v] = True;
#     print(v, end=' ')
#     for w in ladder_index[v]:
#         if not visit[w]:
#             DFS(w)
#
# DFS(0)




