from random import randint as rd


def fillList(list):
  counter = []
  for i in range(0, 10):
    counter.append(0)

  sample = 100
  while(sample > 0):

    n = rd(1, 10)
    counter[n-1] += 1

    sample -= 1

  print(counter)


fillList([])


with open('pi.txt') as obj:
  cont = obj.read()

print(cont)

print(type(cont))


with open('pi.txt') as obj:
  cont = obj.readlines()
  
print(cont)
print(type(cont))
print(cont[0][:10])

with open('writing.txt', 'w') as file:
  file.write('sdfsdfsfsfs')

  