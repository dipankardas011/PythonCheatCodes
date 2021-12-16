cars=["ferrai","bugati","iron man","tata"]
cars.sort()
print(cars)

for i in cars:
    print(i.title())
    # print(f'{i.title()} ')


def isPrime(N)->bool:
    for i in range(2,N):
        if(N%i == 0):
            return False;

    return True

def addPrime(arr):
    """Adding all the prime number between 1-100"""

    for i in range(1,100):
        if isPrime(i):
            arr.append(i)

# normal method
#numbersList = list(range(1,6))
# comprehension method
numbersList = [-i**-1 for i in range(1,6)]
print(numbersList)
print(f'min: {min(numbersList)}')
print(f'max: {max(numbersList)}')


list=[]
addPrime(list)
del list[0] #removing 1
print(f"Prime number list 1-100-> {list}")
print(f"Number of prime number 1-100-> {len(list)}")


# alphabets

alpha = [str(chr(i)) for i in range(65,91)]
print(alpha)
print(alpha[4:15])
print(alpha[:5])
print(alpha[5:])
print(alpha[:])
