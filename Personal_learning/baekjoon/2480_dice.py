# https://www.acmicpc.net/problem/2480

dice = list(map(int, input().split(" ")))
# 각 주사위 눈의 갯수를 체크할 리스트
check = [0] * 7
result = 0

for spot in dice:
    check[spot] += 1

    if check[spot] == 2:
        result = 1000 + (spot*100)
    elif check[spot] == 3:
        result = 10000 + (spot*1000)

if not result:
    result = max(dice) * 100

print(result)
