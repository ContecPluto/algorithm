import sys

sys.stdin = open('10815.txt', 'r')
# sang = input()
# sang_card = list(set(map(int,input().split())))
# answer = int(input())
# answer_card = list(map(int,input().split()))

# for i in answer_card:
#     if i in sang_card:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')







# for i in sang_card:
#     answer_card = answer_card.replace(str(i), '1')
# answer_card = list(map(abs, map(int, answer_card.split())))
# answer_card = [0 if answer_card[i] > 1 else 1 for i in range(answer)]
# print(answer_card)



sang = int(input())
sang_card = list(map(int,input().split()))
answer = int(input())
answer_card = list(map(int,input().split()))
sang_card.sort()

for i in range(len(answer_card)):
    s,l = 0 , sang-1
    c = int((s + l)/2)

    # if sang_card[s] == answer_card[i]:
    #     print(1, end=' ')
    # elif sang_card[l] == answer_card[i]:
    #     print(1, end=' ')
    # else:
    while s != c:
        if answer_card[i] == sang_card[c]:
            print(1, end=' ')
            break
        c = int((s + l)/2)
        if answer_card[i] > sang_card[c]:
            s += 1
        else:
            l -= 1
    else:
        print(0, end=' ')
print()


# for i in range(answer):
#     # print(answer_card)
#     pop_card = answer_card.pop()
#     for j in range(len(sang_card)):
#         if sang_card[j] == pop_card:
#             answer_card.insert(i, 1)
#             del sang_card[j]
#             break
#     else:
#         answer_card.insert(i, 0)
# print(answer_card)

# for i in range(len(answer_card)):
#     s,l = 0 , sang
#     c = int((s + l)/2)
#     if sang_card[s] == answer_card[i]:
#         result[s] += 1
#     elif sang_card[l-1] == answer_card[i]:
#         result[answer-1] += 1
#     else:
#         while s != c:
#             if answer_card[i] == sorted(sang_card)[c]:
#                 # print('찾음', i)
#                 result[i] += 1
#                 break
#             elif answer_card[i] > sorted(sang_card)[c]:
#                 # print('큰쪽', i)
#                 # print(s,c,l)
#                 s = c
#                 c = int((s+l)/2)
#             else:
#                 # print('작은쪽', i)
#                 l = c
#                 c = int((s+l)/2)

# # print(result)
