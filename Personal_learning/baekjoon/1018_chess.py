# https://www.acmicpc.net/problem/1018

M, N = map(int, input().split())

chess = []
for val in range(M):
    chess.append(list(input()))

result = 0xffffffff
for i in range(0, M-7):
    for j in range(0, N-7):
        start_W = 0
        start_B = 0
        start = "W"
        for x in range(i, i+8):
            if result < start_W and result < start_B: break
            for even in range(j, j+8, 2):
                if chess[x][even] == start:
                    start_B += 1
                else:
                    start_W += 1
            
            for odd in range(j+1, j+8, 2):
                if chess[x][odd] == start:
                    start_W += 1
                else:
                    start_B += 1
            start = "B" if start == "W" else "W"
        result = min(start_W, start_B, result)
print(min(result))