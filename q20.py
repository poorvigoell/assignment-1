#program that takes a list of numbers as input and returns their sum

list = []
n = int(input("Enter number of elements : "))
sum = 0

for i in range(0, n):
	element = int(input())
	list.append(element) 
	sum = sum + element

print("the list is: ", list)
print("the sum of the numbers: ", sum)