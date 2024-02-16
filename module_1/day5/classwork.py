# if prime multiply by 10 if not keep value in f(x)
from module import check_primenum, multiplicationtable, pass_to_func

number = int(input("Enter a number: "))
if(check_primenum(number)):
    multiplicationtable(number)
else:
    print(pass_to_func(number))

        
#from foldername.filename import .....
