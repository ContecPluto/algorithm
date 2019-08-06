import sys
sys.stdin= open('1259.txt', 'r')

T = int(input())
for num in range(T):    
    number = int(input())
    P = list(map(int,input().split()))
    
    Metal = []
    P.reverse()
    for i in range(0,len(P),2):
        Metal.append(P.pop())
        Metal.append(P.pop())
        P.insert(0, Metal)
        Metal=[]
    # P.sort()

    for i in range(1):
        for k in range(number-1):
            for j in range(len(P)):
                if P[i][0] == P[j][1]:
                    # print(P[j])
                    P.insert(i, P.pop(j))
                    # print(P)
    
    for i in range(len(P)-1):
        if P[i][1] != P[i+1][0]:
            for j in range(len(P)):
                if P[i][1] == P[j][0]:
                    P.insert(i+1,P.pop(j))
            # print(P[j])
            # print(P)
                

 
                
    # print(P)
    string = ''
    for e in P:
        string += '{0} {1} '.format(e[0], e[1])
    print('#{} {}'.format(num+1, string))
        

            

                    






        
    

