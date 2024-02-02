
# A = [
#      [2,3,4],
#      [3,4,5],
#      [5,6,7]
#     ]
# B = [
#      [1,2,3],
#      [4,5,6],
#      [7,8,9]
#     ]
# C = [
#      [0,0,0],
#      [0,0,0],
#      [0,0,0]
#     ]


# for i in range(len(A)):
#     for j in range(len(A[i])):
#         C[i][j] =A[i][j] + B[i][j]

# print(C)

# D = [1,2,3,4,5,6,7,98,12,434545,6]
# temp_value = D[0]
# for element in D:
#     if (element > temp_value):
#         temp_value = element
#     max_value = temp_value
# print(max_value)


# A = [1,2,3,4,56,7,8,9,23,4,5,6,780,1,3,90,436,78,346,3467,12]
# B = []

# C = []

# for element in A:
#     if(element % 2==0):
#         B.append(element)
#     else:
#         C.append(element)

# print(B,C)

#list_comprehension

# C = [1,2,3,4,56,7,8,9,23,4,5,6,780,1,3,90,436,78,346,3467,12]
# D = [element+2 for element in C]
# even = [element for element in C if element %2 ==0]
# odd = [element for element in C if element % 2 != 0]
# print(even, odd)

list = [2,-5,7,9,-12,9,0,-8,-56,34,-12,56]

positive = [element for element in list if element > 0 ]
negative = [element for element in list if element < 0 ]

print(len(negative),max(positive))
positive.sort()
print(positive)