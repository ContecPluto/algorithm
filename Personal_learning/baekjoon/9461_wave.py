# https://www.acmicpc.net/problem/9461
import sys

# tc = int(input())
tc = int(sys.stdin.readline())
arr = [1, 1, 1]
def wave(n):
    if len(arr) > n:
        return arr[n]
    else:
        for i in range(n - len(arr) + 2):
            arr.append(arr[-2] + arr[-3])
        return arr[n]


for t in range(tc):
    # N = int(input())
    N = int(sys.stdin.readline())
    print(wave(N-1))
