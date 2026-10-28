# Create list1 containing names of five students
list1 = ["Amit", "Priya", "Rahul", "Neha", "Karan"]

# Create list2 containing student names and marks
list2 = [
    ["Amit", 85],
    ["Priya", 92],
    ["Rahul", 78],
    ["Neha", 95],
    ["Karan", 88]
]

print("Original Student List:", list1)

# (a) Search for a student name and display index
search_name = input("\nEnter student name to search: ")

if search_name.title() in list1:
    print("Student found at index:", list1.index(search_name.title()))
else:
    print("Student name not found in the list.")

# (b) Sort names in ascending and descending order
list1.sort()
print("Ascending Order using sort():", list1)

list1.sort(reverse=True)
print("Descending Order using sort():", list1)

print("Ascending Order using sorted():", sorted(list1))
print("Descending Order using sorted():", sorted(list1, reverse=True))

# (c) Add, insert, and remove student names
list1.append("Pooja")
print("After adding a student:", list1)

list1.insert(2, 'rekha')
print("After adding a student:", list1)

list1.remove('rekha')
print("After removing a student:", list1)

# (d) Display all student records using a loop
print("\nAll Student Records:")
for student in list2:
    print("Name:", student[0], "| Marks:", student[1])

# (e) Find student with highest marks and calculate average
highest_student = max(list2, key=lambda student: student[1])
print("\nStudent with Highest Marks:", highest_student[0])
print("Highest Marks:", highest_student[1])

total_marks = sum(student[1] for student in list2)
average_marks = total_marks / len(list2)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# (f) Display number of student records
print("\nNumber of Student Records:", len(list2))