import sys
sys.stdin= open('4839.txt', 'r')

T = int(input())
for num in range(1,T+1):
    P = list(map(int,input().split()))
    count = 1
    result = []

    for i in range(1,3):
        # print(i)
        l = 1
        r = P[0]
        c= int((l+P[0])/2)

        while l != c:
            print(l, c, r)
            if c == P[i]:                
                # print(l, c, r)
                break
            # print(l, c, P[0])
            if c < P[i]:
                l = c
                c= int((l+r)/2)
                count += 1
            else:
                r = c
                c = int((l+c)/2)
                count += 1
        result.append(count)
        count = 1
        print()
    # print(result)

    if result[0] == result[1]:
        print('#{} 0'.format(num))
    elif result[0] > result[1]:
        print('#{} B'.format(num))
    else:
        print('#{} A'.format(num))

    
    
        
            


    
    
    

    

    
        




    
