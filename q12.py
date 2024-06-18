#calculate the sum of digits of a given number

num = input("enter a number: ")
sum = 0
for i in range(len(num)):
    sum = sum + int(num[i])
print("the sum of digits: ", sum)