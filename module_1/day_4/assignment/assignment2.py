# generate multiplication table from 1 to 20
def check_prime(num):
    count = 0
    prime = False
    for i in range(1, num+1):
        if num % i == 0:
            count +=1
    if count ==2:
        prime = True
    return prime

def prime_multi_table():
    for num in range(1, 21):
        if check_prime(num):
            print(f"\n Multiplication table of prime number {num}:\n")

            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")

prime_multi_table()

