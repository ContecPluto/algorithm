import sys
sys.setrecursionlimit(10**8)

def calculation(index):
    global result
    if len(word) - 1 == index:
        result += 1
        return

    cnt = 0
    for i in range(index, len(word)):
        value = False
        if str(word[i]).isdigit():
            if 1 <= i < len(word) - 1:
                x, y, z = map(str, [word[i-1], word[i], word[i+1]])
                X, Y, Z = x.isdigit(), y.isdigit(), z.isdigit()
                if not X and Y and Z:
                    calculation(i+1)
                    value = True

            if i < len(word) - 2:
                x, y, z = map(str, [word[i], word[i+1], word[i+2]])
                X, Y, Z = x.isdigit(), y.isdigit(), z.isdigit()
                if X and not Y and Z:
                    calculation(i+2)
                    value = True

                if X and Y and not Z:
                    calculation(i+2)
                    value = True
        if value:
            break


result = 0
word = list(input())
visit = [False] * len(word)
calculation(0)
# calculation(input())
print(result)


# word = list(input())
# result = 1
# index = 0
# for i in range(len(word)):
#     if str(word[i]).isdigit():
#         value = 0
#         if 1 <= i < len(word) - 1:
#             x, y, z = map(str, [word[i-1], word[i], word[i+1]])
#             X, Y, Z = x.isdigit(), y.isdigit(), z.isdigit()
#             if not X and Y and Z:
#                 value += 1

#         if i < len(word) - 2:
#             x, y, z = map(str, [word[i], word[i+1], word[i+2]])
#             X, Y, Z = x.isdigit(), y.isdigit(), z.isdigit()
#             if X and not Y and Z:
#                 value += 1

#             if X and Y and not Z:
#                 value += 1
#         if value != 0:
#             result += value
# print(result)