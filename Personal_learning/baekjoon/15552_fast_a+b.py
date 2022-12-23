# https://www.acmicpc.net/problem/15552
import sys; sys.stdin = open("15552.txt", "r")

T = int(input())

for i in sys.stdin.readlines():
    A, B = map(int, i.rstrip("\n").split(" "))
    print(A + B)