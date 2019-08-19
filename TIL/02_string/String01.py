

print(ord('A'))
for i in range(65, 91):
    print(chr(i), end = ' ')


arr = 'algorithm'
print(arr[::-1])
arr = list(arr)
arr.reverse()
print(arr)
n = len(arr)
for i in range(n//2):
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
print(arr)
print(''.join(arr))


print('패턴')

arr = 'algorithm'
t=  'asfsfasfewafwafsadfasxcvsdfalgorithmasfasfdaefwfsad'
n, m=len(t), len(arr) #n: 텍스트의 길이, m:패턴의길이

for i in range(n-m+1):
    for j in range(m):
        if t[i + j] != arr[j]:
            break
    else:
        print((t[i:i+m]))

print('while ')
for i in range(n-m+1):
    j=0
    while j<m:
        if t[i + j] != arr[j]:
            break
        j += 1

    if j == m:
        print((t[i:i+m]))


i=j=0
while i<n:
    if arr[j] == t[i]:
        i, j = i+1, j+1
        if j == m:
            print(t[i-j:])
            break
            # j=0       #여러개 찾음
    else:
        i = i - j + 1
        j = 0



