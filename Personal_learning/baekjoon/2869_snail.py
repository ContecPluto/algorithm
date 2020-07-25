A, B, V = list(map(int, input().split()))
N, M = [V-B, A-B]
print(N//M + 1) if N % M else print(N//M)