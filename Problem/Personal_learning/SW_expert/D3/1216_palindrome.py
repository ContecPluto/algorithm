#실패함

import sys
sys.stdin = open('1216.txt', 'r')

for num in range(1):
    arr=[]
    max_arr=0
    num = input()
    for i in range(100):
        numbers = input()
        arr.append(numbers)
        
    # print(num,len(arr[0]))

    for i in range(len(arr)+1):
        # print(arr[i])
        for j in range(i, len(arr[i])):
            cheak = ''
            for k in range(j, len(arr[i])):
                cheak += arr[i][k]
                # print(i, arr[i][k], end = ' ')
                if cheak[::-1] == cheak[::1] and max_arr < len(cheak):
                    # print(cheak)
                    max_arr = len(cheak)
            print(cheak)


        for j in range(i, len(arr[i])):
            cheak = ''
            for k in range(j, len(arr[i])):
                cheak += arr[k][i]
                # print(i, arr[i][j], end = ' ')
                if cheak[::-1] == cheak[::1] and max_arr < len(cheak):
                    # print(cheak)
                    max_arr = len(cheak)

    print(num, max_arr)


           
                


    
