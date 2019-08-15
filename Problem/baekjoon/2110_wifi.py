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

    while arr[len(arr)-1] != home[len(home)-1]:
        if 0< home[c] - home[c-1] <= max_length:
            # print('작을때', s,c, l)
            arr.append(home[c])
            s = c
            l = N
            c= (s + l)//2
            # print(arr)
        else:
            # print(s, c, l)
            l = c
            c = (s + l)//2

        # print(arr)
        # if len(set(arr)) >= C:
        #     break


        count += 1
        if count == 50: break
    arr = sorted(list(set(arr)))
    # print(arr)
    
    i = 0
    while True:
        if not arr[i+2:i+3:]: break
        if arr[i+2] - arr[i] <= max_length:
            # print(arr[i], arr[i+2], arr[i+2] - arr[i], max_length)
            del arr[i+1]
        i += 1
    

    # arr = set(arr) - set(del_arr)

    if len(arr) == C:
        # print(result, max_length)
        result = max(result, max_length)
    # print(max_length, len(arr), C)
    print(max_length,arr)
print(result)
    

            
        

   

    
