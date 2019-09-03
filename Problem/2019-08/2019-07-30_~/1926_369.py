N= list(range(1, int(input())+1))
for i in N:
    count = 0
    i = str(i)
    count += i.count('3')
    count += i.count('6')    
    count += i.count('9')
    if count == 0:
        print(i, end = ' ')
    else:
        print('-'*count, end = ' ')

    

