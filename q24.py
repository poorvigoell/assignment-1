#simple calculator

print("enter the operator:\n 1. add +\n 2. subtract -\n 3. multiply *\n 4. divide /\n 5. exit")
n = int(input("enter the operator: "))

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

if n==1:
    sum = a+b
    print("the sum is: ", sum)

elif n==2:
    diff = a-b
    print("the difference is: ", diff)

elif n==3:
    product = a*b
    print("the product is: ", product)

elif n==4:
    div = a/b
    print("the division is: ", div)

elif n==5:
    print("calculator has been exited.")