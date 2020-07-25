from sys import stdin
input = stdin.readline

T = int(input())
result = ""
for tc in range(T):
    H, W, N = map(int, input().split())
    num = N % H
    if num == 0:
        num = H
    result += str(num) + str((N-1) // H + 1).zfill(2) + "\n"
print(result, end="")