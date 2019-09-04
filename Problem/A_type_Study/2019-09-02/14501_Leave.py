import sys; sys.stdin = open('14501.txt', 'r')

def back(i, start, k):

    for i in range(start, N):
        if start + consulting[i][0] <= 7:
            check.append(start)
            back(i, sum(check) + consulting[i][0], k)kkl
        print(check)




N = int(input())
consulting = [list(map(int, input().split())) for _ in range(N)]
result = []
print(consulting)
for i in range(N):
    for j in range(N):
        check = [i]
        k =2
        back(i, i + consulting[i][0], k)
print(check)
