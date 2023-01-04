# https://www.acmicpc.net/problem/2231
import sys; sys.stdin = open('2231.txt')

# 브루트포스는 모든 경우의수를 대조해보는 알고리즘으로
# 약간의 조건을 추가하여 시간 및 메모리를 비약적으로 감소시킬 수 있다.

num = int(input())
result = 0

# 부분합과 타겟의 숫자차이는 크지 않음.
# 문제에서 요구하는 조건에 따르면 9가 알맞은것으로 보임.
# 변수는 백준의 정답리스트중에서 가져온것이다.
x = num - len(str(num)) * 9

# 부분합의 숫자는 원본의 절반 이상을 절대로 넘을수 없다.
start = max(x, num // 2)
for i in range(start, num):
    res = i + sum(map(int, str(i)))

    if num == res:
        result = i
        break


    

print(result)