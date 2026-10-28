# Create a list of ten integers using range()
numbers = list(range(1, 11))

# (a) Display list and access elements
print("Original List:", numbers)

print("Positive Indexing (index 2):", numbers[2])
print("Negative Indexing (index -1):", numbers[-1])
print("Slicing (index 2 to 6):", numbers[2:7])

# (b) Update an element at a user-specified index
index = int(input("Enter index to update (0-9): "))
if 0 <= index < len(numbers):
    value = int(input("Enter new value: "))
    numbers[index] = value
    print("Updated List:", numbers)
else:
    print("Invalid index!")

# (c) List concatenation and repetition
print("Concatenation (+):", numbers + [11, 12])
print("Repetition (*):", numbers * 2)

# (d) Membership operators
num = int(input("Enter a number to search: "))
print("Number exists (in):", num in numbers)
print("Number does not exist (not in):", num not in numbers)

# (e) List methods
numbers.append(20)
print("After append(20):", numbers)

numbers.insert(2, 30)
print("After insert(2, 30):", numbers)

numbers.remove(30)
print("After remove(30):", numbers)

removed = numbers.pop()
print("Popped Element:", removed)
print("After pop():", numbers)

numbers.reverse()
print("After reverse():", numbers)

count_num = int(input("Enter a number to count: "))
print("Count of", count_num, ":", numbers.count(count_num))

# (f) Sort in ascending and descending order
numbers.sort()
print("Ascending Order using sort():", numbers)

numbers.sort(reverse=True)
print("Descending Order using sort():", numbers)

print("Ascending using sorted():", sorted(numbers))
print("Descending using sorted():", sorted(numbers, reverse=True))

# (g) Aliasing and cloning
alias = numbers
clone = numbers.copy()

alias[0] = 100
print("After modifying alias:")
print("Original List:", numbers)
print("Alias List:", alias)
print("Clone List:", clone)

# (h) Maximum, minimum, and length
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Length:", len(numbers))