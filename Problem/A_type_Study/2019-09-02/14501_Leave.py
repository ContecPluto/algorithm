import sys; sys.stdin = open('14501.txt', 'r')

def back(i, start,check):
    for i in range(start, N):
        if sum(check) + consulting[i][0] <= 7:
            check.append(start)
            back(i, sum(check) + consulting[i][0], check)
    if list(set(check)) not in result:
        result.append(list(set(check)))




N = int(input())
consulting = [list(map(int, input().split())) for _ in range(N)]
result = []
print(consulting)
for i in range(N):
    if i + consulting[i][0] <= 7:
        check = [i]
        back(i, i + consulting[i][0], check)
print(result)
