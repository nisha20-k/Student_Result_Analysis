import numpy as np
students = np.array([
    "Aman",
    "Rahul",
    "Priya",
    "Sneha",
    "Karan",
    "Riya",
    "Ankit",
    "Pooja",
    "Neha",
    "Rohit"
])

marks = np.array([
    85,
    72,
    95,
    33,
    67,
    88,
    54,
    91,
    45,
    29
])

print("Students:")
print(students)

print()

print("Marks:")
print(marks)

# Total elements in the array
total_students = len(students)

print("Total Students:", total_students)

# average of total marks
average_marks = np.mean(marks)
print("Average Marks:", average_marks)

#print the highest marks
highest_marks = np.max(marks)
print("Highest marks: ", highest_marks)


# print lowest marks
lowest_marks = np.min(marks)
print("Lowest marks: ", lowest_marks)

# who is the topper of the class

topper_index = np.argmax(marks)
topper_name = students[topper_index]
print("Topper:",topper_name)


#lets find out who score the lowest
lowest_index = np.argmin(marks)
lowest_student = students[lowest_index]
print("Lowest scorer:",lowest_student)

# lets find out pass students

pass_student = marks >=35
print(pass_student)
print("Pass Student:", np.sum(pass_student)) #count the number of pass student


# number of fail students

fail_student = marks<35
print("Fail Student:",np.sum(fail_student))

# find student above Average

above_avg = students[marks > average_marks]
print("Above Average students:",above_avg)