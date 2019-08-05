# 이후 재괴에서 사용함

# arr = 'ABC'
# bit = [0] * 3

# def print_set(bits):
#     for i in range(len(bits)):
#         if bits[i]:
#             print(arr[i], end = ' ')
#     print()

# print_set(arr)

N = 3
bit = [0] * N

for i in range(2):
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for i in range(2):
            bit[2] = i
            print(bit)
            # for i in range(2):
            #     bit[3] = i
                # print(bit)
