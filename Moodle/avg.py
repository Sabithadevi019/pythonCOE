stu_num = input("Enter student number: ")
stu_name = input("Enter student name: ")
marks_c = float(input("Enter marks in C: "))
marks_cp= float(input("Enter marks in C++: "))
marks_java = float(input("Enter marks in Java: "))
total= marks_c + marks_cp + marks_java
avg= total/ 3
if avg< 70:
    result = "Fail"
    grade="Not yet passed no grade displayed"
else:
    result = "Pass"
    if avg>= 90:
        grade = "A"
    elif avg>= 80:
        grade = "B"
    else:
        grade = "C"
print("Student Number:",stu_num)
print("Student Name:",stu_name)
print("Total Marks: ",total)
print("Average Marks:",avg)
print("Result:",result)
print("Grade:",grade)
