
personInfo={
    'name':"Dipankar",
    'id': 2001,
    'loc': 'Jamshedpur',
    'gender': 'male',
    'age': 23
}
# empty dict
aa = {}

print(personInfo)
print(personInfo['name'])

personInfo['xLoc'] = 23
personInfo['yloc']=34


for key, val in personInfo.items():
    print(f'key: {key} \t-> \tvalue: {val}')

print("###############################\n")

for info in sorted(personInfo.keys()):
    print(f"keys '{info}' about all the data")
print("\n\n")
for info in personInfo.values():
    print(f"values '{info}' about all the data")


