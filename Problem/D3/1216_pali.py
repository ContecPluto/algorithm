import sys
sys.stdin = open('1216.txt', 'r')

for num in range(10):
    arr=[]
    max_arr=0
    num = input()
    for i in range(100):
        numbers = input()
        arr.append(numbers)

    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         for k in range(j+1,len(arr[i])+1):
    #             cheak = arr[i][j:k]
    #             if cheak == cheak[::-1] and max_arr < len(cheak):
    #                 max_arr = len(cheak)
    
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         cheak = ''
    #         for k in range(j,len(arr[i])):
    #             cheak += arr[k][i]
    #             if cheak == cheak[::-1] and max_arr < len(cheak):
    #                 max_arr = len(cheak)

    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cheak2 = ''
            for k in range(j+1,len(arr[i])+1):
                cheak = arr[i][j:k]
                cheak2 += arr[k-1][i]
                if cheak == cheak[::-1] and max_arr < len(cheak):
                    max_arr = len(cheak)
                if cheak2 == cheak2[::-1] and max_arr < len(cheak2):
                    max_arr = len(cheak2)
    
    print('#{} {}'.format(num, max_arr))                    
                    