#program that copies content of one text file to another

f=open("q25.txt",'r')
f1=open("sample.txt",'w')

try:
    f1.write(f.read())
    print(f"Contents of '{f}' copied to '{f1}'.")

except FileNotFoundError:
    print(f"Error: File not found - '{f}' or '{f1}'.")

print("Copying completed.")