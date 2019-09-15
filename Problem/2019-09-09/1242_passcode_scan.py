import sys; sys.stdin = open('1242.txt','r')



passcode = {0:[3, 2, 1, 1], 1:[2, 2, 2, 1], 2:[2, 1, 2, 2], 3:[1, 4, 1, 1], 4:[1, 1, 3, 2], 5:[1, 2, 3, 1], 6:[1, 1, 1, 4],
            7:[1, 3, 1, 2], 8:[1, 2, 1, 3], 9:[3, 1, 1, 2]}
num = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
num2 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

T = int(input())
for tc in range(1, T+1):
    password = []
    N, M = list(map(int, input().split()))
    for i in [input() for _ in range(N)]:
        temp = ''
        for j in range(M-1):
            if temp:
                if i[j] != '0':
                    temp += i[j]
                else:
                    if i[j+1] != '0':
                        temp += i[j]
            else:
                if i[j] != '0':
                    temp += i[j]
        if temp and temp not in password:
            password.append(temp)
    # print(password)

    for ps in password:
        result = []
        x = ps
        check = []
        result = []
        c = len(x) - 1
        for i in x:
            if not i.isdecimal():
                number = num.get(i)
                for j in range(3, -1, -1):
                    if number >= (2 ** j):
                        number -= (2 ** j)
                        result.append('1')
                    else:
                        result.append('0')
            else:
                number = int(i)
                for j in range(3, -1, -1):
                    if number >= (2 ** j):
                        number -= (2 ** j)
                        result.append('1')
                    else:
                        result.append('0')

        result = []
        for a in range(0, len(x), 7):
            # print(a)
            check = [0, 0, 0, 0]
            k = '0'
            q = 0
            # print(x[a:a + 7])
            for i in x[a: a+7]:
                # print(i==k,i ,k)
                if k == i:
                    check[q] += 1
                else:
                    k = i
                    q += 1
                    if q > 3:
                        break
                    check[q] += 1
            # print(check)
            # print(check, a)
            for idx, k in enumerate(passcode.values()):
                if check == k:
                    # print('7자')
                    result.append(idx)
                    break
            else:
                q = 0
                k = '0'
                check = [0, 0, 0, 0]
                # print(x[a: a + 14])
                for i in x[a: a + 14]:
                    # print(i==k,i ,k)
                    if k == i:
                        check[q] += 1
                    else:
                        k = i
                        q += 1
                        if q > 3:
                            break
                        check[q] += 1
                else:
                    for i in range(4):
                        check[i] = check[i] // 2
                    # print(check)
                    for idx, k in enumerate(passcode.values()):
                        # print(check, k)
                        if check == k:
                            # print('14자')
                            result.append(idx)

        # print(result)
        if len(result) == 8:
            print(result)
            even = 0
            odd = 0
            for i in range(8):
                if i % 2:
                    odd += result[i]
                else:
                    even += result[i]

            if (odd + (even * 3)) % 10 == 0:
                print('#{} {}'.format(tc, sum(result)))
            else:
                print('#{} 0'.format(tc))

