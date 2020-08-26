from sys import stdin
input = stdin.readline

def DFS(zone, s):
    visit[s] = True
    for p in G[s]:
        if p in zone and visit[p] == False:
            DFS(zone, p)

    
N = int(input())
area = list(map(int, input().split()))
G = [[] for _ in range(N)]
result = 0xfffffff

for i in range(N):
    information = list(map(int, input().split()))
    for j in range(1, information[0] + 1):
        G[i].append(information[j]-1)   

for subset in range(1 << N):
    A, B = [], []
    for j in range(N):
        if subset & (1 <<j):
            A.append(j)
        else:
            B.append(j)
            
    if A and B:
        for zone in (A, B):
            visit = [False] * N
            DFS(zone, zone[0])
            for i in zone:
                if visit[i] == False:
                    break
            else:
                continue
            break
        else:
            value = [0, 0]
            idx = 0
            for zone in (A, B):
                for population in zone:
                    value[idx] += area[population]
                idx += 1
            result = min(result, abs(value[0] - value[1]))

if result == 0xfffffff:
    result = -1
print(result)