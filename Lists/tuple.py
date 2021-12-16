point = (1,5)
# tuples are immutable
# point[0]=2
print(point)

point = (4,6)
print(point)

# Some more list stuffs

toppings = ['mushrooms', 'onions','pinapple']
print('abc' not in toppings)
print('onions' in toppings)

if(toppings):
    print("Has toppings\n")
else:
    print("no toppings\n")
# C has NULL
# C++ has nullptr & NULL
# JAVA has null
# Python has none



# dict within dict
users ={}

for i in range(5):
    print("Enter your name and age")
    Str = input("Name: ")
    age = int(input("Your age: "))

    temp = {}
    temp['name']=Str
    temp['age']=age
    users[i] = temp

print(users)


# remove all the strings that starts with all
arrStr = ['alldog','cat','whales','elephants','all']

print(arrStr)

for i in arrStr:
    if(i.startswith('all')):
        arrStr.remove(i)

# remove all the strings that are all
# while arrStr[0].startswith('all'):
#     arrStr.remove('all')

print(arrStr)