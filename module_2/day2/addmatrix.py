# add two matrix of 3*3
# A = [[2,3,4],[3,4,5],[1,2,3]]
# B = [[1,2,1],[4,5,6],[2,3,1]]
# sum = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A[i])):
#             sum[i][j] = A[i][j] + B[i][j]

# for c in sum:
#     print(c)

# find maximum value
# A = [1,2,3,4,4,5,6,43,2,42,5,4,90,346,4,436]
# largest = A[0]
# for element in A:
#     if(element > largest):
#         largest = element
#     max_value = largest
# print(max_value)

# #separate odd and even number in another list
# A = [1,2,3,4,5,6,7,8,9,11,23,54,24]
# even, odd = [], []

# # for element in A:
# #     if(element % 2 == 0):
# #         even.append(element)
# #     else:
# #         odd.append(element)

# #list comprehension
# even = [element for element in A if element %2 == 0]
# odd = [element for element in A if element %2 != 0]
# print(f"Even list = {even}, Odd list = {odd}")
# # list comprehension
# C = [element+3 for element in A]
# print(C)

A = [1,3,4,5,6,-9,0,9,-4,-8,2,-7,-3]
positive = [element for element in A if element > 0]
negative = [element for element in A if element < 0]
print(max(positive),len(negative))
positive.sort()
print(positive)

        