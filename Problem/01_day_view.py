import sys

sys.stdin = open('input.txt', 'r')
N = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(2, len(arr)-2):
    for j in range(arr[i]+1, 0, -1):
        for k in range(-2, 2, 1):
            if k == 0 : continue
            elif arr[i]-j <= arr[i+k]:
                break
        else:
            count += 1

print(count)

