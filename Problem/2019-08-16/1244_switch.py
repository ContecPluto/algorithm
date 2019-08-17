import sys
sys.stdin = open('1244.txt','r')

switch = int(input())
boolean = list(map(int, input().split()))
student_number = int(input())
student = [list(map(int, input().split())) for i in range(student_number)]


for i in range(student_number):
    if student[i][0] == 1:
        # print('남자')
        check = student[i][1]
        for k in range(check-1, switch, check):
            if boolean[k] == 1:
                boolean[k] = 0                
            else:
                boolean[k] = 1
    else:
        check = student[i][1] -1
 

        for k in range(0, check+1):
            # print(check-k, check+k, check)
            if boolean[check-k] == boolean[check+k]:
                if boolean[check-k] == 1:
                    boolean[check-k] = 0                
                    boolean[check+k] = 0                
                else:
                    boolean[check-k] = 1
                    boolean[check+k] = 1
            else:
                break

        # print('여자')
print(boolean)









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
        
            

