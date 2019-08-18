import sys
sys.stdin = open('1244.txt','r')

switch = int(input())
boolean = list(map(int, input().split()))
student_number = int(input())
student = [set(map(int, input().split())) for i in range(student_number)]


for i, j in student:
    if i == 1:
        boolean[j-1::j] = [not k for k in boolean[j-1::j]]
    else:
        j -= 1
        for k in range(1, j+1):
            if boolean[j-k] != boolean[j+k]:
                k -= 1
                boolean[j-k:j+k+1] = [not z for z in boolean[j-k:j+k+1]]
                break
        else:
            boolean[j-k:j+k+1] = [not z for z in boolean[j-k:j+k+1]]

boolean = list(map(str, map(int, boolean)))
for i in range(switch//20 + 1):
    print(' '.join(boolean[i*20:i*20+20:]))


# a=[1,0,1,0]
# a[1:3] = [not i for i in a[1:3]]
# print(a)








# for i, j in student:
#     j -= 1   
    
#     if i == 1:
#         for k in range(j, switch, j+1):
#             if boolean[k] == 1:
#                 boolean[k] = 0                
#             else:
#                 boolean[k] = 1
#         # print('남성')
#     else:
#         for k in range(0, j+1):
#             # print(j-k, j+k, j)
#             if boolean[j-k] == boolean[j+k]:
#                 if k == 0:
#                     if boolean[j] == 1:
#                         boolean[j] = 0                
#                     else:
#                         boolean[j] = 1 
#                 else:
#                     if boolean[j-k] == 1:
#                         boolean[j-k] = 0                
#                     else:
#                         boolean[j-k] = 1

#                     if boolean[j+k] == 1:
#                         boolean[j+k] = 0                
#                     else:
#                         boolean[j+k] = 1  
#             else: break
        
            

