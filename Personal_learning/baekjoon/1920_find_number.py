from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
numbers = list(map(int, input().split()))
answer = ""

for number in numbers:
    start = 0
    end = N - 1
    check = "0"
    while start <= end:
        mid = (start+end) // 2
        if A[mid] < number:
            start = mid + 1
        elif A[mid] > number:
            end = mid - 1
        elif A[mid] == number:
            check = "1"
            break
    answer += check + "\n"
print(answer, end="")
