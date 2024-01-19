def check_prime(num):
    count = 0
    prime=False
    for i in range (1 , num+1):
        if num % i == 0:
            count = count+1
    if (count ==2):
        return True
    return prime

num = int(input("Enter a number to check prime: "))
value_of_check_prime = check_prime(num)

if value_of_check_prime:
    print("Prime Number")
    
def multiplication(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
for num in range (1,31):    
    multiplication(num)
        
else:
    print("It is not a prime number")
