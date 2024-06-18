#program to check if a substring is present in a given substring

str = input("enter a string:")
substr = input("enter a substring:")

if substr in str:
    print("the substring is present in the given string")
else:
    print("the substring is not present in the given string")