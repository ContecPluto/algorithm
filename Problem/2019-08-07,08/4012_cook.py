# import sys
# sys.stdin = open('4012.txt','r')

# T=int(input())
# for num in range(3):
#     N = int(input())
#     table = [list(map(int,input().split())) for _ in range(N)]
#     menu = [0]*(N//2)
#     result = 20000
#     c_list = [1*i for i in range(N)]
#     cheak = []
#     m_cheak = []


#     for x in range(len(cheak), N):
#         for y in range(x, N):
#             if x != y:
#                 cheak.append([x,y])
#     print(cheak)
    
#     for i in range(len(cheak)):
#         c_list = [1*i for i in range(N)]
#         for j in cheak[i]:
#             c_list.remove(j)
#         for x in range(N):
#             for y in range(x, N):
#                 if x != y:
#                     cheak.append([x,y])
#         cheak.append(c_list)
#     print(cheak)


#순열 테스트

def permutation(arr,r):
    i=0
    tri = num = 0
    result = []
    per = []
    count = [0]*len(arr)
    while i<10:
        if len(result) >= r:
            per.append(result)
            result=[]
        for j in range(len(arr)):
            if count[j]:
                
            if not count[j]:
                result.append(arr[j])

            
            


print(permutation('ABCD', 2))
# permutation([1, 2, 3, 4, 5], 3)


        
            




