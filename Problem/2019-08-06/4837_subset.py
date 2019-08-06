import sys
sys.stdin= open('4837.txt', 'r')

T = int(input())
for num in range(1,T+1):
    N, K = list(map(int,input().split()))
    arr = [i for i in range(1,13)]
    n = len(arr)
    # print(arr)
    total = []
    count = 0
    
    for subset in range(1<<n):
        # print(subset, end = '>')
        for i in range(n):
            if subset & (1 << i):
                # print(arr[i], end =' ')
                total.append(arr[i])
            
        if len(total)==N and sum(total) == K:
            count +=1
            # print(total, K, end = ' ')
        total = []
        # print()
    print('#{} {}'.format(num, count))

