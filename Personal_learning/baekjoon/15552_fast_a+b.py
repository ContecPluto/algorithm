# https://www.acmicpc.net/problem/15552
import sys
sys.stdin = open("15552.txt", "r")
input = sys.stdin

T = int(input.readline())

result = []
for i in input.readlines():
    result.append(f"{sum(map(int, i.split(' ')))}")

sys.stdout.write("\n".join(result))