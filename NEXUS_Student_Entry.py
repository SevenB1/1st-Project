Students_List = []
print("========== STUDENT ENTRY SYSTEM ==========")
n = int(input("Number of Students: "))
for i in range(n):
    print("Student Id      Student Name         Subject 1     Subject 2     Subject 3")
    student_info = input("Enter the information asked above separated by commas: ")
    info = student_info.split()
    students_list = info
    Students_List.append(students_list)
for i, students_list in enumerate(Students_List):
    print(students_list)