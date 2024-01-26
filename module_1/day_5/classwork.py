from modules import is_prime, multiplication, pass_to_func

num = int(input("Enter a number to check prime: "))

if not is_prime(num):
    print (f"{num} is a prime number.")
    multiplication(num)
else:
    print (f"{num} is a prime number.")
    pass_to_func(num)
    print(pass_to_func(num))