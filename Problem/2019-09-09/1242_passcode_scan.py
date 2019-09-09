
passcode = {0:[3, 2, 1, 1], 1:[2, 2, 2, 1], 2:[2, 1, 2, 2], 3:[1, 4, 1, 1], 4:[1, 1, 3, 2], 5:[1, 2, 3, 1], 6:[1, 1, 1, 4],
            7:[1, 3, 1, 2], 8:[1, 2, 1, 3], 9:[3, 1, 1, 2]}
num = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
num2 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

x = '1ADC58D764DBB7'
check = []
c = len(x) - 1
for i in x:
    if not i.isdecimal():
        check.append(num.get(i)*(16**c))
    else:
        check.append(int(i)*(16**c))
    c -= 1
# print(check)
print(sum(check))
x = sum(check)
i = 0
check = []
while 2**i < x:
    i+=1
for j in range(i-1, -1, -1):
    if x >= (2**j):
        print('큼')
        x -= (2**j)
        check.append(1)
    else:
        print('작음')
        check.append(0)
    print('마지막',x)
    print(check)
print(check)



# # print(0, end='')
# for i in '1DB176C588D26EC':
#     print('시작',i)
#     if not i.isdecimal():
#         i = num.get(i)
#     i = int(i)
#     j = 3
#     while i != 0:
#         # print(i, j)
#         # print(i // (2**j))
#         if i // (2**j) != 0:
#             check[j] += '1'
#             i -= 2**j
#
#         j -= 1
#     print(int(check))
#
#
#     print('',end=' ')
#
# print(int('1DB176C588D26EC', 16))
# number = []
# for a in range(0, len(x), 7):
#     # print(a)
#     # for i in range(10):
#     check = [0,0,0,0]
#     k = '0'
#     q = 0
#     # print(x[a:a+7])
#     if x[a] != '1':
#         for i in x[a: a+7]:
#             # print(i==k,i ,k)
#             if k == i:
#                 check[q] += 1
#             else:
#                 k = i
#                 q += 1
#                 check[q] += 1
#         # print(check)
#     else:
#         for i in x[a-7: a+7]:
#             # print(i==k,i ,k)
#             if k == i:
#                 check[q] += 1
#             else:
#                 k = i
#                 q += 1
#                 if q > 3:
#                     break
#                 check[q] += 1
#         print(x[a:a+7])
#         print(x[a-7:a])
#         print(x[a - 7: a + 7])
#         print('14',check)
#
#
#     print(check)
#     for idx, k in enumerate(passcode.values()):
#         # print(check, k)
#         if check == k:
#             print(idx)

