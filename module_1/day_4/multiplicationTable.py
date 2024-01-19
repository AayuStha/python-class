def multiplication(num):
    for i in range(1,11):
        # print(num, 'x', i, '=', num*i)
        print(f"{num} x {i} = {num*i}")
num = int(input("Enter a number: "))
for num in range (1,11):    
    multiplication(num)
