def multiplicationtable(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
        
number = int(input("Enter a number: "))
for i in range(1,number+1):
    multiplicationtable(i)