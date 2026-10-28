# Q3: Tuple Operations

t = (10, 20, 30, 20, 40, 50, 60, 20, 70, 80)

# a) Display tuple, indexing and slicing
print("Tuple:", t)
print("Positive Indexing:", t[2])
print("Negative Indexing:", t[-2])
print("Slicing:", t[2:6])

# b) Concatenation and repetition
t2 = (90, 100)
print("Concatenation:", t + t2)
print("Repetition:", t * 2)

# c) Membership operators
num = 20
print("20 exists:", num in t)
print("20 does not exist:", num not in t)

# d) Maximum, minimum and length
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Length:", len(t))

# e) Count occurrences
value = int(input("Enter value to count: "))
print("Occurrences:", t.count(value))

# f) Search using index()
value = int(input("Enter value to search: "))

if value in t:
    print("Element found at index:", t.index(value))
else:
    print("Element not found")