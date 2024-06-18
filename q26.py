#program that checks if a string starts with a given prefix or ends with with a given suffix

prefix = input("enter a prefix: ")
suffix = input("enter a suffix: ")
text = input("enter a string: ")

if text.startswith(prefix):
    print(text, "starts with the prefix ", prefix)

if text.endswith(suffix):
    print(text, "ends with the suffix ", suffix)