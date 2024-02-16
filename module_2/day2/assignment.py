# list prime number from a list using list comprehension

numbers = [2, 4, 6, 8, 3, 5, 7, 9, 13, 34, 57, 87, 34, 65, 92]
prime_numbers = [num for num in numbers if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print(prime_numbers)