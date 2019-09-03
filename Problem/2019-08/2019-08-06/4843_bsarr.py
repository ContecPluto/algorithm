import sys
sys.stdin= open('4843.txt', 'r')

T = int(input())
for num in range(1,T+1):
    number = int(input())
    arr = list(map(int,input().split()))

    for i in range(number - 1):
        minidx = i
        for j in range(i + 1, number):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    
    for i in range(0,10,2):
        arr.insert(i,arr.pop())
    
    for i in range(number-1):
        if len(arr) != 10:
            arr.pop()
                
    print('#{} {}'.format(num, ' '.join(map(str, arr))))
            





