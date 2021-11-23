
print("hello world")

a = list()

a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)

print(a)

b = {
  'name': 'dipankar',
  'sex': 'male',
  'age': 23
}

for key, v in b.items():
  print(f"key: {key}")
  print(f"value: {v}")


import json

usr = str(input('Username'))

with open('login.json', 'w') as file:
  json.dump(usr, file)

