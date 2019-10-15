import sys; sys.stdin = open('5249.txt', 'r')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    p = [x for x in range(V+1)]
    Edge,MST = [], []
    cnt, cur = 0, 0
    for i in range(E):
        Edge.append((tuple(map(int, input().split()))))
    Edge.sort(key=lambda x:x[2])

    while len(MST) < V :
        u, v, w = Edge[cur]
        a = find_set(u); b = find_set(v)
        if a != b:
            p[b] = a
            MST.append((u, v, w))
        cur += 1

    for edge in MST:
        cnt += edge[2]
    print('#{} {}'.format(tc, cnt))

