#count the occurrence of an element in a list

list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	element = int(input())
	list.append(element) 

print("the list is: ", list)

char = input("input the element to be counted: ")
count = 0

for i in list:
	if i == 'e':
		count = count + 1

print("Count of ", char, "in the list is : "
	+ str(count))