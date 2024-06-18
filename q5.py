#input a string from user and write it to a text file

file = open("q5.txt", "w")
str = input("enter a string: ")
file.write(str)
file.close()