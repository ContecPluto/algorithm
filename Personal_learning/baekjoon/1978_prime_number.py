N = int(input())
numbers = list(map(int, input().split()))
result = 0
for number in numbers:
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            result += 1
print(result)