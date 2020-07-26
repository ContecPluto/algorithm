from math import sqrt

T = int(input())
result = ""
for tc in range(T):
    x, y = map(int, input().split())
    num = sqrt(y - x)
    num = int(num*2) if num % 1 else int(num*2) - 1 
    result += str(num) + "\n"
print(result, end="")