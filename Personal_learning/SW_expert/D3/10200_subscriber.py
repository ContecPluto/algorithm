import sys; sys.stdin = open("10200.txt", "r")

T = int(input())
result = ""
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    min_cnt = 0 if A + B <= N else (A + B) - N
    result += "#{} {} {}\n".format(tc, str(min(A, B)), str(min_cnt))
print(result, end="")
