random_dict = {}
print(random_dict)

random_dict = {1:"one"}
print(random_dict)

random_dict = {1:"one","two":2}
print(random_dict)

a = {1:"one","two":2}
print(a[1])
print(a["two"])

print(a.get("key"))
print(a.get("two"))
print(a.items())
for key in random_dict:
    print(key, random_dict[key])

print(a.values())

print(a.pop(1))
print(a)

# student = {"name": "John", "age": 20, "grade": "A", "subjects": ["Math", "Science", "History"], "address": {"street": "123 Main St", "city": "ktm", "zipcode": "12345"}}

# print(student.popitem())
# print["address"]["city"]

grades = {
    'Rita': 73,
    'Sammu': 98,
    'Sony': 45,
    'Alish': 102,
    'Ishan': 68,
    'Ankita': 50
}
for values in grades.values():
  print(values)

new_dict = {}
for key,value in grades.items():
      if value > 70:
          new_dict[key] = value
print(new_dict)

new_dict = {key:value for key,value in grades.items() if value>70}
print(new_dict )

s_dict = {key:value for key,value in grades.items() if key[0]=="S"}
print(s_dict)

new_dict = {key:value/2 for key,value in grades.items() if value>70}
print(new_dict )


even_dict = {}
odd_dict = {}
for key, value in grades.items():
     if value % 2 == 0:
         odd_dict[key] = value
     else:
         even_dict[key] = value
print(odd_dict)
print(even_dict)