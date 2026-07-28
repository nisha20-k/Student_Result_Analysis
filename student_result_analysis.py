import csv

import numpy as np

def load_data(filename):
    students = []
    marks = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row["Name"])
            marks.append(int(row["Marks"]))

    return np.array(students), np.array(marks)
students, marks = load_data("student_data.csv")

# students = np.array([
#     "Aman",
#     "Rahul",
#     "Priya",
#     "Sneha",
#     "Karan",
#     "Riya",
#     "Ankit",
#     "Pooja",
#     "Neha",
#     "Rohit"
# ])

# marks = np.array([
#     85,
#     72,
#     95,
#     33,
#     67,
#     88,
#     54,
#     91,
#     45,
#     29
# ])

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
    print("\n" + "=" * 55)
    print("STUDENT REPORT CARD")
    print("=" * 55)

    print(f"{'Name':<12}{'Marks':<8}{'Grade':<8}{'Result'}")
    print("-" * 55)

    for i in range(len(students)):
        grade = calculate_grade(marks[i])
        result = "Pass" if marks[i] >= 35 else "Fail"

        print(f"{students[i]:<12}{marks[i]:<8}{grade:<8}{result}")
    
    
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
    

# Top three student

def display_top_students():
    print("\n" + "=" * 40)
    print("TOP 3 STUDENTS")
    print("=" * 40)

    sorted_indexes = np.argsort(marks)[::-1]

    for i in range(3):
        index = sorted_indexes[i]
        print(f"{i+1}. {students[index]} - {marks[index]} Marks")
 
def generate_report():
    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Marks", "Grade", "Result"])

        for i in range(len(students)):
            grade = calculate_grade(marks[i])
            result = "Pass" if marks[i] >= 35 else "Fail"

            writer.writerow([
                students[i],
                marks[i],
                grade,
                result
            ])

    print("\n✅ report.csv generated successfully!")


def load_data(filename):
    students = []
    marks = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row["Name"])
            marks.append(int(row["Marks"]))

    return np.array(students), np.array(marks)
students, marks = load_data("student_data.csv")



# Grade Statistics

def grade_statistics():
    grades = []
    
    for mark in marks:
        grades.append(calculate_grade(mark))
        
    print("\n" + "=" *40)
    print("GRADE STATISTICS")
    print("=" * 40)
    
    grade_list = ["A+", "A", "B", "C", "D", "F"]
    
    for grade in grade_list:
        count = grades.count(grade)
        print(f"{grade:<2} : {count} Student(s)")
display_summary()
display_grades()
display_top_students()
generate_report()
grade_statistics()        
