def get_student_details():
    student_count = int(input("Enter the number of students: "))
    students = {}

    for _ in range(student_count):
        name = input("Enter the student's name: ")
        roll_no = input("Enter the student's roll number: ")
        total_mark = int(input("Enter the student's total marks: "))
        students[roll_no] = {"name": name, "total_mark": total_mark}

    return students

def find_top_student(students):
    top_student = None
    max_marks = -1

    for roll_no, details in students.items():
        if details["total_mark"] > max_marks:
            max_marks = details["total_mark"]
            top_student = {"roll_no": roll_no, **details}

    return top_student

def main():
    students = get_student_details()
    top_student = find_top_student(students)

    if top_student:
        print("\nDetails of the student with the highest total marks:")
        print(f"Name: {top_student['name']}")
        print(f"Roll Number: {top_student['roll_no']}")
        print(f"Total Marks: {top_student['total_mark']}")
    else:
        print("No student data available.")

if __name__ == "__main__":
    main()
