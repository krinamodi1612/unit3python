import array

# Create an integer array containing eight elements
numbers = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])

# (a) Display array and access elements using indexing and slicing
print("Original Array:", numbers)
print("Element at index 2:", numbers[2])
print("Last element using negative indexing:", numbers[-1])
print("Slicing (index 2 to 5):", numbers[2:6])

# (b) Insert a new element at a specified position
numbers.insert(2, 100)
print(numbers)

# (c) Remove a specified element and the last element
numbers.remove(100)
print(numbers)

numbers.pop()
print(numbers)

# (d) Search for an element and display its index
search_value = int(input("\nEnter element to search: "))

if search_value in numbers:
    print("Element found at index:", numbers.index(search_value))
else:
    print("Element not found in the array.")

# (e) Check membership using in and not in
check_value = int(input("\nEnter element to check membership: "))

print("Element exists (in):", check_value in numbers)
print("Element does not exist (not in):", check_value not in numbers)

# (f) Display maximum, minimum, and length
print("\nMaximum Element:", max(numbers))
print("Minimum Element:", min(numbers))
print("Length of Array:", len(numbers))

# (g) Reverse the array
numbers.reverse()
print("Reversed Array:", numbers)