# from functions import func_upper
# # lambda for x
# # f_x= lambda x: x**2+5*x+3
# # x = f_x(5)
# # print (x)

# # lambda for x and y
# # f_x= lambda x,y: x**2+5*x*y+3
# # xy = f_x(5,2)
# # print(xy)

# # function like lambda 
# def f_x(x):
#     y = x**2+5*x+3
#     return y


# numbers = [1,2,3,4,5,6,7,8,9,10]
# y = [f_x(x) for x in numbers]

# print(y)

# # map example
# map_example=list(map(f_x, numbers))
# print(map_example)

# b = "This is a college simple text to understand function"
# splitted_text= b.split(" ")
# # c = b.upper()
# # ca_lamba= lambda x : x.upper()
# c_lambda=list(map(func_upper, splitted_text))
# join_list = " ".join(c_lambda)
# print(join_list)


my_list = "This is the world where we live and sleep"


def func_assign(word, index):
    if index % 2 == 0:
        d =word.upper()
    else:
        d= word.title()
    return d

print(" ".join([func_assign(word, index) for index, word in enumerate (my_list.split(" "))]))
