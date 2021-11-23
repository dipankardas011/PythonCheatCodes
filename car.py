

class Owner:
  def __init__(self, owner) -> None:
    self.owner = owner
  
  def sit(self):
    print('This function gets overriden')
  

class Car(Owner):
  def __init__(self,o, n, f) -> None:
    super().__init__(o)
    self.name = n
    self.fuel = f

  def sit(self):
    print(f'CarName: {self.name}\tFuel: {self.fuel}')
    print(f'Owner: {self.owner}')

car = Car('Dipankar D', 'tesla','electric')
car.sit()