from sys import stdin
input = stdin.readline

N = int(input())
numbers = [num for num in map(int, input().split()) if num > 1]
result = 0
for number in numbers:
    if number % 2 or number == 2: 
        for i in range(3, number, 2):
            if not number % i:
                break
        else:
            result += 1
print(result)