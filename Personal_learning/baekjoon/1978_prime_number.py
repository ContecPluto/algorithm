from sys import stdin
input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
result = 0
for number in numbers:
    if number != 1 and number % 2 != 0 or number == 2:
        for i in range(3, number//2, 2):
            if number % i == 0:
                break
        else:
            result += 1
print(result)