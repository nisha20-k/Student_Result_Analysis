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


#grade calculation

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 35:
        return "D"
    else:
        return "F"
    
    print("\nGrades")
print("-" * 20)


def display_grades():
    print("\nGrades")
    print("-" * 30)
    for i in range(len(students)):
        grade = calculate_grade(marks[i])
        print(f"{students[i]:<10} : {marks[i]:<5} : {grade}")
        
    
    
     #Professional report
    
topper_index = np.argmax(marks)
lowest_index = np.argmin(marks)

topper_name = students[topper_index]
lowest_student = students[lowest_index]

highest_marks = np.max(marks)
lowest_marks = np.min(marks)

average_marks = np.mean(marks)

pass_count = np.sum(marks >= 35)
fail_count = np.sum(marks < 35)

def display_summary():
    print("\n" + "=" * 50)
    print("SUMMARY REPORT")
    print("=" * 50)

    print(f"Total Students : {len(students)}")
    print(f"Average Marks  : {average_marks:.2f}")
    print(f"Highest Marks  : {highest_marks}")
    print(f"Topper         : {topper_name}")
    print(f"Lowest Marks   : {lowest_marks}")       
    print(f"Lowest Scorer  : {lowest_student}")
    print(f"Pass Students  : {pass_count}")
    print(f"Fail Students  : {fail_count}")
    
display_summary()

display_grades()


# Top three student

def display_top_students():
    print("\n" + "=" * 40)
    print("TOP 3 STUDENTS")
    print("=" * 40)

    sorted_indexes = np.argsort(marks)[::-1]

    for i in range(3):
        index = sorted_indexes[i]
        print(f"{i+1}. {students[index]} - {marks[index]} Marks")
        
display_top_students()