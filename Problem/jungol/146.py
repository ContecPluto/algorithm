n= int(input())
count = 0
count2 = 0

for i in range(n):
    for j in range(n-i):
        print(chr(65+count), end=' ')
        count += 1
    for k in range(n-j-1):
        print(count2, end=' ')
        count2 +=1
    print()
