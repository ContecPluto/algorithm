import sys; sys.stdin = open('1242.txt','r')

passcode = {0:[3, 2, 1, 1], 1:[2, 2, 2, 1], 2:[2, 1, 2, 2], 3:[1, 4, 1, 1], 4:[1, 1, 3, 2], 5:[1, 2, 3, 1], 6:[1, 1, 1, 4],
            7:[1, 3, 1, 2], 8:[1, 2, 1, 3], 9:[3, 1, 1, 2]}
num = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
num2 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}


T = int(input())
for tc in range(T):
    final_check = []
    # print('시작',tc+1)
    final = []
    password = []
    N, M = list(map(int, input().split()))
    for i in [input() for _ in range(N)]:
        temp = ''
        for j in range(M):
            if temp:
                if i[j] != '0':
                    temp += i[j]
                else:
                    if temp and temp in password:
                        temp = ''
                    else:
                        for k in range(1, 4):
                            if j+k < M:
                                if i[j+k] != '0':
                                    temp += i[j]
                                    break
                        else:
                            if temp and temp not in password:
                                last_check = ''
                                for i2 in range(len(temp)-1, -1, -1):
                                    last_check = temp[i2] + last_check
                                    if last_check in password:
                                        temp = ''
                                        break
                                else:
                                    password.append(temp)
                                    temp = ''
            else:
                if i[j] != '0':
                    temp += i[j]
        if temp and temp not in password:
            password.append(temp)
    print(password)
    for ps in password:
        # print(ps)
        result = ''

        for i in ps:
            # result = bin(int(ps, 16))[2::]

            if not i.isdecimal():
                number = num.get(i)
                for j in range(3, -1, -1):
                    if number >= (2 ** j):
                        number -= (2 ** j)
                        result += '1'
                    else:
                        if result:
                            result += '0'
            else:
                number = int(i)
                for j in range(3, -1, -1):
                    if number >= (2 ** j):
                        number -= (2 ** j)
                        result += '1'
                    else:
                        if result:
                            result += '0'
        # print(result)
        code = []
        while len(code) != 8:
            result = '0' + result
            start = 0
            end = 5000
            code = []
            length = 0
            while start != end:
                end = start
                length += 1
                for k in range(8, 0, -1):
                    if len(code) == 8:
                        break
                    check = [0, 0, 0, 0]
                    c_index = 0
                    c_check = 0
                    for j in map(int, result[start: start + 7 * k]):
                        if c_check == j:
                            check[c_index] += 1
                        else:
                            c_check = j
                            c_index += 1
                            if c_index > 3:
                                break
                            check[c_index] += 1
                    else:
                        if c_index != 3:
                            continue

                        if k >= 2:
                            for div in range(len(check)):
                                check[div] //= k
                        for j in range(10):
                            if passcode.get(j) == check:
                                code.append(j)
                                start += 7 * k
                                break
                        if passcode.get(j) == check:
                            break
                # print(length, code, len(code))
                if length != len(code):
                    break
        if len(code) == 8:
            even = 0
            odd = 0
            for i in range(len(code)):
                if i % 2:
                    odd += code[i]
                else:
                    even += code[i]
            if (odd + (even * 3)) % 10 == 0:
                final.append(sum(code))

    print('테스트케이스', tc+1, sum(final))












