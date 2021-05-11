a = int(input("1. sayıyı giriniz: "))
b = int(input("2. sayıyı giriniz: "))

for x in range(a,a+1):
  if x % 15 == 0:
    print("FizzBuzz")
  elif x % 5 == 0:
    print("Buzz")  
  elif x % 3 == 0:
    print("Fizz")
  else:
    print(x)

for y in range(b,b+1):
  if y % 15 == 0:
    print("FizzBuzz")
  elif y % 5 == 0:
    print("Buzz")  
  elif y % 3 == 0:
    print("Fizz")
  else:
    print(y) 
