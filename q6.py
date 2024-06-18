#program to read and print the contents of a file

f=open("q6.txt", 'r') 
content = f.read()

for i in content:
    print(i, end="")

f.close()