#program that returns minimum and maximum value of numbers in a list

list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	element = int(input())
	list.append(element) 
	
list.sort()
print("the minimum value: ", list[0])
print("the maximum value: ", list[n-1])