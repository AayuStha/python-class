#generate multiplication table of prime number from 1 to 20.
def check_primenum(number):
    count = 0 
    prime = False
    for i in range(1, number+1):
        if(number % i == 0):
            count += 1
    if(count == 2):
        prime = True    
    return prime
def multiplicationtable(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number*i}")
def main():
    for number in range(1,21):
        if check_primenum(number):
            print(f"\nMultiplication table of prime number {number}:\n")
            multiplicationtable(number)

main()
                
# f(x)= x^2+5*x+2
