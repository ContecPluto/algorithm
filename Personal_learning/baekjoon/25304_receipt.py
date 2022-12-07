# https://www.acmicpc.net/problem/25304

cash = int(input())
line = int(input())

total = 0

for idx in range(line):
    product, num = map(int, input().split(" "))
    total += product * num

print("Yes" if total == cash else "No")