import sys; sys.stdin = open('1242.txt','r')



passcode = {0:[3, 2, 1, 1], 1:[2, 2, 2, 1], 2:[2, 1, 2, 2], 3:[1, 4, 1, 1], 4:[1, 1, 3, 2], 5:[1, 2, 3, 1], 6:[1, 1, 1, 4],
            7:[1, 3, 1, 2], 8:[1, 2, 1, 3], 9:[3, 1, 1, 2]}
num = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
num2 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}


T = int(input())
for tc in range(1, 9):
    final = []
    # print('시작',tc)
    final = []
    password = []
    N, M = list(map(int, input().split()))
    for i in [input() for _ in range(N)]:
        temp = ''
        for j in range(M-1):
            if temp:
                if i[j] != '0':
                    temp += i[j]
                else:
                    for k in range(4):
                        if j+k < M:
                            if i[j+k] != '0':
                                temp += i[j]
                                break
            else:
                if i[j] != '0':
                    temp += i[j]
        if temp and temp not in password:
            password.append(temp)
    # print(password)
    for ps in password:
        print(ps)
        result = []
        c = len(ps) - 1

        for i in ps:
            if not i.isdecimal():
                number = num.get(i)
                for j in range(3, -1, -1):
                    if number >= (2 ** j):
                        number -= (2 ** j)
                        result.append(1)
                    else:
                        if result:
                            result.append(0)
            else:
                number = int(i)
                for j in range(3, -1, -1):
                    if number >= (2 ** j):
                        number -= (2 ** j)
                        result.append(1)
                    else:
                        if result:
                            result.append(0)

        # print(result)
        pwd = []
        # for _ in range(8):
        while len(pwd) != 8:
            pwd = []
            start = 0
            result.insert(0, 0)
            # print('반복중', tc)
            for x in range(0, len(result)-1, 7):
                # print(x)
                # print(result[x:x+7])
                x += start
                if x >= len(result)-1:
                    break

                for __ in range(1,11):
                    check = [0, 0, 0, 0]
                    c = 0
                    k = 0
                    for i in result[x:x+(7*__)]:
                        if k == i:
                            check[c] += 1
                        else:
                            k = i
                            c += 1
                            if c > 3:
                                break
                            check[c] += 1
                    if __ == 2:
                        for div in range(len(check)):
                            if check[div] %2 ==0:
                                check[div] //= 2
                            # print(check)
                    for j in range(10):
                        if check == passcode.get(j):
                            # print(__)
                            if __ == 2:
                                start += 7
                                # print(1)
                            pwd.append(j)
                            break
                    if check == passcode.get(j):
                        break
                # if check == passcode.get(j):
                #     break


            if len(pwd) == 8:
            # print(pwd)
                even = 0
                odd = 0
                for i in range(len(pwd)):
                    if i % 2:
                        odd += pwd[i]
                    else:
                        even += pwd[i]

                if (odd + (even * 3)) % 10 == 0:
                    final.append(sum(pwd))
                    # print('#{} {}'.format(tc, sum(pwd)))
                # else:
                #     print('#{} 0'.format(tc))

    print('#',tc, sum(final))






