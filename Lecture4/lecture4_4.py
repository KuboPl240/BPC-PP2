students = {
    "Alice": [("Math", 4), ("Science", 5), ("English", 4)],
    "Bob": [("Math", 2), ("Science", 1), ("English", 3)],
    "Charlie": [("Math", 5), ("Science", 4), ("English", 4)]
}

student_about_4 = []
for student_name, course_list in students.items():
    about_4 = True
    for course_name, evaluation in course_list:
        if evaluation<4:
            about_4 = False
    if about_4:
        student_about_4.append(student_name)
        

print("Students who have evaluation about 4 in every courses: ", student_about_4)
