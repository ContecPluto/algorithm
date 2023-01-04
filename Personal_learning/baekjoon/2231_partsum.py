import sys; sys.stdin = open('2231.txt')

num = input()
target = int(num)
N = len(num)
result = 0

for i in range(int(num)):
    res = i
    
    for j in str(i):
        res += int(j)

    if (target == res):
        result = i
        break

print(result)