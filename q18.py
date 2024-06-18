#program to check if two strings are anagrams of each other

str1 = input("enter a string:")
str2 = input("enter another string:")

sorted1 = sorted(str1)
sorted2 = sorted(str2)

if sorted1==sorted2:
    print("the strings are anagrams.")
    
elif sorted1!=sorted2:
    print("the strings are not anagrams.")