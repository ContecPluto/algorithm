import sys
sys.stdin = open('2110.txt', 'r')

N, C = list(map(int, input().split()))
home = [int(input()) for _ in range(N)]
home.sort()
result = 0

for max_length in range(1, home[len(home)-1]):
    arr = [home[0]]
    s = 0
    l = N-1
    c= (s + l)//2
    count = 0

    for i in range(1, N):
        if home[i] - home[i-1] <= max_length:            
            arr.append(home[i])
        else:
            break
    if len(arr) > 2:
        for i in range(len(arr)-2):
            if arr[i+2] - arr[i] <= max_length:
                del arr[i+1]
            else:
                break
    print(arr)

   
    

 
# print(result)
    

            
        

   

    
