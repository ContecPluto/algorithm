import sys; sys.stdin = open('2798.txt', 'r')


# def comb(s, p, result):
#     global answer
#     if p == 3:
#         answer = max(answer, result)
#         return
#     for i in range(s, N):
#         if result + arr[i] > M: continue
#         comb(i+1, p+1, result + arr[i])
#
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# answer = 0
# comb(0, 0, 0)

def blackjack():
    answer = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                check = arr[i] + arr[j] + arr[k]
                if check < M:
                    answer = max(answer, check)
                elif check == M:
                    return check
                else:
                    break
    return answer


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
print(blackjack())