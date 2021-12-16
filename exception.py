
num = int(input('numerator: '))
deno = int(input('denometator: '))

try:
  ff = num/deno
  print(ff)
except ZeroDivisionError:
  print("division by zero")
  # for faliing silently
  # pass
except FloatingPointError:
  print("Floating point error")
else:
  print("other errors")

title = "disdfsd,sdfsdf"
print(title.split(','))
