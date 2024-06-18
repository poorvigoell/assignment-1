#program that converts temperature from fahrenheit to celcius or vice-versa

print("what is the unit of temperature\n 1. celcius\n 2. fahrenheit")
unit = input("enter 1 or 2: ")
value = int(input("enter the temperature value: "))

if unit=="1":
    temp1 = (value * 9/5) + 32
    print("the temperature in Fahrenheit is: ", temp1)

elif unit=="2":
    temp2 = (value - 32) * 5 / 9 
    print("the temperature in Celcius is: ", temp2)