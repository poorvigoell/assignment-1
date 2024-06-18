#program that removes all punctuation from a string

test_str = input("input a string: ")

print("The original string is: ", test_str)

# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Removing punctuations in string
for ele in test_str:
	if ele in punc:
		test_str = test_str.replace(ele, "")

print("The string after punctuation filter: ", test_str)