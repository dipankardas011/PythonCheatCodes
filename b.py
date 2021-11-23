
b=int(input('Enter any number > '))


def isPrime(N, i):
  """
  @return true when prime number
  @return false otherwise
  """
  if i == N:
    return True

  if N%i == 0:
    return False
  
  return isPrime(N, i+1)

# variable length argument length
def printVarArgs(*args):
  for iter in args:
    print(iter)
  print()


def buildProfile(first, last, **info):
  """Build a dict"""
  info['firstName'] = first
  info['lastName'] = last
  return info


print(isPrime(b,2))

printVarArgs('hello')
printVarArgs('hello','world')
printVarArgs('hello','world','dipa23')

user=buildProfile("dipankar", "das", location="jsr", age=24)

for k,v in user.items():
  print(f"{k} | value: {v}")