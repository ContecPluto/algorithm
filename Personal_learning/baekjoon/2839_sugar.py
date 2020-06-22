# https://www.acmicpc.net/problem/2839

sugar = int(input())
bag = 0
N = sugar // 3
for val in range(N):
    if sugar % 5 == 0:
        bag += sugar//5
        sugar = 0
        break
    bag += 1
    sugar -= 3

if sugar == 0:
    print(bag)
else:
    print(-1)