# a= 0b1010
# b = a&1

# print(b)

# print(a)
# #<< 왼쪽으로 비트이동 2**n 으로 곱해줌
# print(a<<1)
# print(a<<2)
# print(a<<3)
# #>> 오른쪽으로 비트이동 2**n 으로 나눠줌
# print(a>>1)
# print(a>>2)

# #a의 우측번째 수에 왼측의 수가 들어있는지 확인합니다.
# #있다면 0이아닌수를 출력합니다.

# print(a&(2<<1))


# arr = [3,6,7,1,5,4]
# N= len(arr)

# for subset in range(1 << N):
#     print(subset, end = '>')
#     for j in range(N):
#         if subset & (1 <<j):
#             print(arr[j], end=' ')
#         # print()
#     print()


# arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]
# N = len(arr)
# count = 0
# a_sum = []

# for subset in range(1 << N):
#     for j in range(N):
#         if subset & (1<<j):
#             a_sum.append(arr[j])
#     if sum(a_sum) == 0 and a_sum:
#         count += 1
#         print(subset, '>', a_sum, count)        
#     a_sum = []
    
a= 1
a=3 if a==1 else 2
print(a)
