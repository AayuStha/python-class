def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
        return True

def pass_to_func(x):
    return x**2 + 5*x + 2

def multiplication(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")