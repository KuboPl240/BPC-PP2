
students = {
    "Alice": [("Math", 4), ("Science", 5), ("English", 3)],
    "Bob": [("Math", 2), ("Science", 1), ("English", 3)],
    "Charlie": [("Math", 5), ("Science", 5), ("English", 4)]
}


def average_evaluation(student_name):
    courses = students.get(student_name, [])
    total_score = sum([evaluation for course, evaluation in courses])
    return total_score / len(courses)


def best_student():
    best_student = None
    best_avg = float('inf')
    for student_name, courses in students.items():
        avg = average_evaluation(student_name)
        if avg < best_avg:
            best_avg = avg
            best_student = student_name
    return best_student


def sort_students():
    return sorted(students.keys(), key=average_evaluation)


print("Average evaluation of Alice:", average_evaluation("Alice"))
print("Best student:", best_student())
print("Students sorted from best to worst:", sort_students())