# for i in range(1,10,2):
#     print(i)

#prime number
num = int(input("Enter a number: "))
count = 0
for i in range(1, num+1):
    if(num % i == 0):
        count += 1

if(count == 2):
    print("num is prime")
else:
    print("num isnt prime")

    
