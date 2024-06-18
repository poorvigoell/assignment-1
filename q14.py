#program to input multiple lines of code till empty line is entered

lines = []
print("Enter lines of text (press Enter on an empty line to finish): ")

while True:
    line = input()
    if line == "":
        break  
    lines.append(line) 

print("\nYou entered:")

for line in lines:
    print(line)