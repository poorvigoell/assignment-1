#check if a number is odd or even

num = int(input("enter a number: "))
if (num != 0):
    if (num%2 == 0):
        print("the number is even")
    else:
        print("the number is odd")
else:
    print("the number is zero")
