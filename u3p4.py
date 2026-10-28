# Accept two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# (a) Display strings and their lengths
print("\nFirst String:", str1)
print("Length of First String:", len(str1))

print("Second String:", str2)
print("Length of Second String:", len(str2))

# (b) Access characters using positive and negative indexing
print("\nFirst Character (positive indexing):", str1[0])
print("Last Character (negative indexing):", str1[-1])

if len(str2) > 0:
    print("First Character of Second String:", str2[0])
    print("Last Character of Second String:", str2[-1])
else:
    print("Second string is empty.")

# (c) Extract substrings using slicing
print("\nFirst String (first 3 characters):", str1[:3])
print("First String (characters from index 1 to 4):", str1[1:5])
print("Second String (first 3 characters):", str2[:3])
print("Second String (characters from index 1 to 4):", str2[1:5])

# (d) String repetition and concatenation
print("\nRepeated First String (* 2):", str1 * 2)
print("Concatenated Strings (+):", str1 + str2)

# (e) Check whether a character or substring exists
sub = input("\nEnter a character or substring to search: ")

print("Substring exists in first string:", sub in str1)
print("Substring does not exist in first string:", sub not in str1)

# (f) Compare two strings
print("\nstr1 == str2:", str1 == str2)
print("str1 != str2:", str1 != str2)
print("str1 < str2:", str1 < str2)
print("str1 > str2:", str1 > str2)

# (g) Convert strings to uppercase and lowercase
print("\nFirst String in Uppercase:", str1.upper())
print("First String in Lowercase:", str1.lower())
print("Second String in Uppercase:", str2.upper())
print("Second String in Lowercase:", str2.lower())